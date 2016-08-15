
import numpy as np
from matplotlib import pyplot
import spm1d



#(0) Load dataset:
dataset      = spm1d.data.uv1d.t2.PlantarArchAngle()
yA,yB        = dataset.get_data()  #normal and fast walking





#(1) Compute confidence intervals:
alpha      = 0.05
ci0        = spm1d.stats.ci_pairedsample(yA, yB, alpha, datum='difference', mu=0)
ci1        = spm1d.stats.ci_pairedsample(yA, yB, alpha, datum='meanA', mu='meanB')
ci2        = spm1d.stats.ci_pairedsample(yA, yB, alpha, datum='meanA', mu='tailsAB')
print( ci0 )
print( ci1 )
print( ci2 )
### compute incorrect CIs for demonstration:
ciA_bad    = spm1d.stats.ci_onesample(yA, alpha)
ciB_bad    = spm1d.stats.ci_onesample(yB, alpha)




#(2) Plot:
pyplot.close('all')
pyplot.figure(figsize=(14,7))
pyplot.get_current_fig_manager().window.move(0, 0)


### plot means and standard deviations:
ax     = pyplot.subplot(231)
spm1d.plot.plot_mean_sd(yA)
spm1d.plot.plot_mean_sd(yB, linecolor='r', facecolor='r', edgecolor='r')
ax.set_title('Means and SDs')



### plot hypothesis test results:
ax     = pyplot.subplot(232)
spmi   = spm1d.stats.ttest_paired(yA, yB).inference(alpha, two_tailed=True)
spmi.plot(ax=ax)
spmi.plot_threshold_label()
ax.set_title('Hypothesis test')
ax.text(0.6, 0.2, 'Datum: zero\nCriterion:  $t ^*$', transform=ax.transAxes)




### plot confidence interval for mean paired difference:
ax     = pyplot.subplot(233)
ci0.plot(ax=ax)
ax.set_title('CI  (possibility 1)')
ax.text(0.1, 0.8, 'Datum: difference\nCriterion: mu=0', transform=ax.transAxes)



### plot confidence interval for mean paired difference:
ax     = pyplot.subplot(234)
ci1.plot(ax=ax)
ax.set_title('CI  (possibility 2)')
ax.text(0.1, 0.4, 'Datum: meanA\nCriterion: meanB', transform=ax.transAxes)


### plot confidence interval for mean paired difference:
ax     = pyplot.subplot(235)
ci2.plot(ax=ax)
ax.set_title('CI  (possibility 3)')
ax.text(0.1, 0.4, 'Datum: meanA\nCriterion: tailsAB', transform=ax.transAxes)


### plot CIs computed separately for the means (INCORRECT!!!)
ax     = pyplot.subplot(236)
ciA_bad.plot(ax=ax)
ciB_bad.plot(ax=ax, linecolor='r', facecolor='r', edgecolor='r', alpha=0.3)
ax.set_title('CIs computed separately for each group', size=10)
ax.text(0.1, 0.4, 'INCORRECT!!!', transform=ax.transAxes)





pyplot.show()



