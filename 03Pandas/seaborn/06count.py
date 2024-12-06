# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
sns.set_style('whitegrid')

fig = plt.figure(figsize=(15, 5))
axe1 = fig.add_subplot(131)
axe2 = fig.add_subplot(132)
axe3 = fig.add_subplot(133)

sns.countplot(x='class', palette='Set1', data=titanic, ax=axe1)
sns.countplot(x='class', hue='who', palette='Set2', data=titanic, ax=axe2)
sns.countplot(x='class', hue='who', palette='Set3', dodge=False, data=titanic, ax=axe3)

axe1.set_title('titanic class')
axe2.set_title('titanic class - who')
axe3.set_title('titanic class - who(stacked)')

plt.show()
