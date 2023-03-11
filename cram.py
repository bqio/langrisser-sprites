# https://segaretro.org/Sega_Mega_Drive/Palettes_and_CRAM

from struct import unpack as up

TOTAL_COLORS = 64

# https://gendev.spritesmind.net/forum/viewtopic.php?t=2188
def pallete_4bpp_convert_color(n: int) -> int:
	return (0, 49, 87, 119, 146, 174, 206, 255)[n >> 1]

def pallete_4bpp_to_rgb(n: int) -> tuple[int]:
	return (pallete_4bpp_convert_color(n >> 0 & 0xE),
        	pallete_4bpp_convert_color(n >> 4 & 0xE),
        	pallete_4bpp_convert_color(n >> 8 & 0xE))

def pallete_4bpp_from_file(file_path: str) -> list[tuple[int]]:
	pallete = []
	with open(file_path, "rb") as fp:
		for _ in range(TOTAL_COLORS):
			pallete.append(pallete_4bpp_to_rgb(up("<H", fp.read(2))[0]))
	return pallete