from cairosvg import svg2png
import argparse
import sys

svg = \
"""
<svg width="1920" height="1080" xmlns="http://www.w3.org/2000/svg" style="background-color:#B02318">
  <g id="Layer_1">
    <title>{game}: {category}</title>
    <rect id="title_bar" height="240" width="1840" y="40" x="40" stroke-width="5" stroke="#ffffff" fill="#54bace"/>
    <text xml:space="preserve" text-anchor="middle" font-family="sans-serif" font-size="60" id="title" y="180" x="960" stroke-width="0" stroke="#ffffff" fill="#fffcfc">
      {game}: {category}
    </text>
    <foreignObject x="40" y="280" width="1840" height="760">
      <p xmlns="http://www.w3.org/1999/xhtml" 
         style="color:white;font-size:50px;text-align:center;position:absolute;top:50%;left:50%;
                transform: translate(-50%, -50%);font-family:sans-serif">
        {description}
        <br/>
        ({year})
      </p>
    </foreignObject>
    <rect id="svg_4" height="760" width="1840" y="280" x="40" stroke-width="5" stroke="#ffffff" fill="none"/>
  </g>
</svg>
"""

def name_for_game(c):
  if c == "gamers":
    return "House of Gamers"
  elif c == "mouse":
    return "House of Mouse"
  elif c == "hose":
    return "Hose of Gamers"

def generate_svg(args):
  out = svg.format(game=name_for_game(args.game), 
                   category=args.category,
                   description=args.description,
                   year=args.year)
  print(out, file=sys.stdout)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description = 'Generate House of Games SVG')
  parser.add_argument('-g', '--game', help='Type of game', choices=['gamers', 'mouse', 'hose'], required=True)
  parser.add_argument('-c', '--category', help='Category string',  required=True)
  parser.add_argument('-y', '--year', help='Year string',  required=True)
  parser.add_argument('-d', '--description', help='Description string', required=True)
  parser.set_defaults(func=generate_svg)

  args = parser.parse_args()
  if not vars(args):
    parser.print_help(sys.stderr)
  else:
    args.func(args)
