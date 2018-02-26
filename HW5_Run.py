import HW5 as lol
import scr.SamplePathClass as SamplePathSupport
import scr.FigureSupport as Fig
headProb = 0.5
timeSteps = 20
realizationNumber = 1000

print ('The probability of getting a head is 0.5, and 20 flips/experiment, and 1000 experiments.')

myCohort = lol.Realization(id = 2, realization_number = realizationNumber, head_prob = headProb)
myCohort.simulate(timeSteps)

print ('Average expected reward (dollors):', myCohort.get_ave_exp_value())
print ('The maximum reward is:', max(myCohort._expValue), "dollars, and the minimum reward is:", min(myCohort._expValue), 'dollars.')



# plot the histogram
Fig.graph_histogram(
    observations=myCohort.get_expValue(),
    title='Histogram of Rewards',
    x_label='Reward',
    y_label='Count')

#estimate the prob of losing money in this game
probLoss = myCohort.get_loss_num()
print ('The probability of losing money in this game is:', probLoss)
