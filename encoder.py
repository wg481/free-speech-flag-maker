from PIL import Image
import sys
import math

WIDTH = 1920
HEIGHT = 1080

def main(input_file, output_file):
	with open(input_file, "r", encoding="utf-8") as f:
		data = f.read()

	chunks = [data[i:i+6] for i in range(0, len(data), 6)]
	colors = [c for c in chunks if len(c) == 6]
	leftovers = "".join(c for c in chunks if len(c) < 6)

	image = Image.new("RGB", (WIDTH, HEIGHT), (0, 0, 0))
	pixels = image.load()

	n = len(colors)
	if n == 0:
		image.save(output_file)
		print("No colors generated.")
		return

	for i, hex_color in enumerate(colors):
		r = int(hex_color[0:2], 16)
		g = int(hex_color[2:4], 16)
		b = int(hex_color[4:6], 16)

		x_start = math.floor(i * WIDTH / n)
		x_end = math.floor((i + 1) * WIDTH / n)

		for x in range(x_start, x_end):
			for y in range(HEIGHT):
				pixels[x, y] = (r, g, b)

	image.save(output_file)

	if leftovers:
		print("Leftover characters:")
		print(leftovers)
	else:
		print("No leftover characters.")

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage: python encoder.py input.txt output.png")
		sys.exit(1)

	main(sys.argv[1], sys.argv[2])

