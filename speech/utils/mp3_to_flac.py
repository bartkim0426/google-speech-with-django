from pydub import AudioSegment


def mp3_to_flac(file_name):
    mp3_full_name = file_name + ".mp3"
    audio = AudioSegment.from_mp3(mp3_full_name)
    audio = audio.set_channels(1)
    bitrate = audio.frame_rate
    flac_full_name = file_name + ".flac"
    audio.export(flac_full_name, format='flac')
    return bitrate
