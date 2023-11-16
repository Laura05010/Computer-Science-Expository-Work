import numpy as np
import sounddevice as sd
import math

C_NATURAL = 261.63

# def generate_beep(frequency, duration, volume=0.5):
#     """
#     <frequency>:    frequency in Hz
#     <duration>:     duration in seconds
#     <volume>:       volume from 0.0 to 1.0
#     """
#     # Calculate the time axis
#     t = np.linspace(0, duration, int(duration * 44100), False)
    
#     # Generate a sine wave for the given frequency (beep)
#     return volume * np.sin(2 * np.pi * frequency * t)

# def play_beep(beep) -> None:
#     sd.play(beep)
#     sd.wait()

def play(frequency, duration, volume=0.5):
    """
    <frequency>:    frequency in Hz
    <duration>:     duration in seconds
    <volume>:       volume from 0.0 to 1.0
    """
    # Calculate the time axis
    t = np.linspace(0, duration, int(duration * 44100), False)
    
    # Generate a sine wave for the given frequency (beep)
    sine_wave = volume * np.sin(2 * np.pi * frequency * t)
    sd.play(sine_wave)
    sd.wait()

# def play(frequency=C_NATURAL, duration=1, volume=0.1) -> None:
    # play_beep(generate_beep(frequency, duration, volume))
    # play_beep_2(frequency, duration, volume)

def calibrated_sound() -> None:
    note = 4 * C_NATURAL
    play(note, 0.1, 0.1)
    play(note, 0.1, 0.1)

    # Wait 1 second
    play(0, 1, 0)

# def dist_to_note(distance):
#     return (3 * math.exp(-((0.007 * distance) ** 2)) + 1) * C_NATURAL

def play_distance(distance) -> None:
    # print(dist_to_note(distance))
    # play(dist_to_note(distance), 0.2, 0.1)
    play((3 * math.exp(-((0.007 * distance) ** 2)) + 1) * C_NATURAL, 0.2, 0.1)

def main() -> None:
    """
    Note: 
    Smallest noticable difference in frequency is roughly 0.05 * C_NATURAL.
    This is ignored in favour of a continuous distance -> frequency function.
    """

    # Play baseline
    play()

if __name__ == "__main__":
    main()
