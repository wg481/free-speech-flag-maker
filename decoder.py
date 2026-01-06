from PIL import Image
import sys

def parse_leftovers(arg):
	if not arg.startswith("--leftovers="):
		return []

	hex_string = arg.split("=", 1)[1].strip().lower()

	if len(hex_string) not in (2, 4):
		raise ValueError("Leftovers must be 1 or 2 bytes (2 or 4 hex characters).")

	if any(c not in "0123456789abcdef" for c in hex_string):
		raise ValueError("Leftovers contain invalid hex characters.")

	return [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]


def main(input_image, output_text, leftovers):
	image = Image.open(input_image).convert("RGB")
	width, height = image.size
	pixels = image.load()

	colors = []
	last_color = None

	# Detect vertical color regions
	for x in range(width):
		color = pixels[x, 0]
		if color != last_color:
			colors.append(color)
			last_color = color

	# Convert colors to hex tokens
	tokens = []
	for r, g, b in colors:
		tokens.append(f"{r:02x}")
		tokens.append(f"{g:02x}")
		tokens.append(f"{b:02x}")

	# Append leftovers
	tokens.extend(leftovers)

	# Write output
	with open(output_text, "w", encoding="utf-8") as f:
		for i, token in enumerate(tokens):
			f.write(token)
			if (i + 1) % 16 == 0:
				f.write("\n")
			else:
				f.write(" ")

	print(f"Decoded {len(colors)} colors.")
	if leftovers:
		print(f"Appended leftovers: {' '.join(leftovers)}")
	print(f"Output written to {output_text}")


if __name__ == "__main__":
	if len(sys.argv) < 3 or len(sys.argv) > 4:
		print("Usage: python decoder.py input.png output.txt [--leftovers=xx|xxxx]")
		sys.exit(1)

	leftovers = []
	if len(sys.argv) == 4:
		try:
			leftovers = parse_leftovers(sys.argv[3])
		except ValueError as e:
			print(f"Error: {e}")
			sys.exit(1)

	main(sys.argv[1], sys.argv[2], leftovers)
