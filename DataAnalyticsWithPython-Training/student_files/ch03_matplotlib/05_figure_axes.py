import matplotlib.pyplot as plt

figure = plt.figure(figsize=(8, 4))

# note: axisbg was deprecated in older versions of matplotlib, 
# if you have an older version, use a line like this one instead:
# sub221 = figure.add_subplot(221, axisbg='#ffffcc')  # for matplotlib versions < 2.0
sub221 = figure.add_subplot(221, facecolor='#ffffcc')
sub221.text(0.5, 0.5, s='subplot(221)', ha='center', va='center', fontsize=20, alpha=.5, color='#287171')

sub222 = figure.add_subplot(222, facecolor='#4455cc')
sub222.text(0.5, 0.5, 'subplot(222)', ha='center', va='center', fontsize=20, color='#5511aa')

sub223 = figure.add_subplot(223, facecolor='#aa5422')
sub223.text(0.5, 0.5, 'subplot(223)', ha='center', va='center', fontsize=20, color='g')

sub224 = figure.add_subplot(224, facecolor='#ccddee')
sub224.text(0.5, 0.5, 'subplot(224)', ha='center', va='center', fontsize=20,
            color='#ff0000')

plt.show()

