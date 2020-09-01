import thinkdsp
import matplotlib.pyplot as pyplot

cos_sig = thinkdsp.CosSignal(440,1.0,0)
sin_sig = thinkdsp.SinSignal(880,0.5,0)

mix = cos_sig+sin_sig

wave = mix.make_wave(duration=0.5, start=0, framerate=11025)
period = mix.period
segment = wave.segment(0,period*3)
#segment.plot()
#pyplot.show()

wave.write(filename = "output.wav")

spectrum = wave.make_spectrum()
#spectrum.plot()
