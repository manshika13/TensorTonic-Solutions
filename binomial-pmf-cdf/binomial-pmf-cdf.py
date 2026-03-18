import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """

    if not isinstance(n,(int,np.integer)) or n<0:
        raise ValueError(f"n must be a non-negative integer,got {n}")
    if not isinstance(k,(int,np.integer)) or k<0 or k>n:
        raise ValueError(f"n must be a non-negative,got {n}")
    if not (0.0 <=p<=1.0):
        raise ValueError(f"p must be in [0,1],got {p}")
    # for edge cases
    if p==1.0:
        pmf=1.0 if k==n else 0.0
        cdf=0.0 if k<n else 1.0
        return (float(pmf),float(cdf))
    # Stable computation using log-spae (avoids factorial overflow)
    # PMF=C(n,k)*p^k * (1-p)^(n-k)
    #log(PMF)=log(C(n,k))+k*log(k) +(n-k)*log(1-p)
    log_pmf=(np.log(comb(n,k,exact=False))+k*np.log(p)+(n-k)*np.log1p(-p))
    pmf=float(np.exp(log_pmf))
    
    #CDF 
    # Each term computed in log-space for numerical stability,then accumulated
    log_q=np.log1p(-p)
    log_p=np.log(p)

    cdf=0.0
    for i in range(k+1):
        log_pmf_i=(np.log(comb(n,i,exact=False))+i*log_p+(n-i)*log_q)
        cdf+=np.exp(log_pmf_i)
    cdf=float(np.clip(cdf,0.0,1.0))

    return (pmf,cdf)
    