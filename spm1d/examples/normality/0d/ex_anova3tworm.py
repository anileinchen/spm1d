
import numpy as np
import scipy.stats
import spm1d
import spm1d



#(0) Load dataset:
dataset      = spm1d.data.uv0d.anova3tworm.NYUHiringExperience()
dataset      = spm1d.data.uv0d.anova3tworm.Southampton3tworm()
y,A,B,C,SUBJ = dataset.get_data()
print dataset



#(1) Conduct normality test:
np.random.seed(0)
alpha      = 0.05
spmi       = spm1d.stats.normality.anova3tworm(y, A, B, C, SUBJ).inference(alpha)
print( spmi )


