from stories import Story

default_story = Story(["place", "noun", "verb", "adjective", "plural_noun"], """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""", "Default Story")

pizza_party = Story(["plural_noun_1", "adjective", "song_title", "celebrity", "feeling", "verb", "location", "food", "plural_noun_2", "person"], """I just got back from a pizza party with {person}. Can you believe we got to eat {adjective} pizza in {location}?! Everyone got to choose their own toppings. I made '{food} and {plural_noun_1}' pizza, which is my favorite! They even stuffed the crust with {plural_noun_2}. How {feeling}! If that wasn't good enough already, {celebrity} was there singing {song_title}. I was so inspired by the music, I had to get up out of my seat and {verb}.""", "The Pizza Party")

the_queen = Story(["noun", "location_1", "adverb", "clothing", "adjective_1", "plural_noun", "verb", "adjective_2","location_2","phrase_or_saying"], """Today I met the Queen of {location_2} during a quick trip to {location_1}. I had left the house because I really needed to pick up a dozen {adjective_1} {plural_noun} in order to repair my {noun}. I wasn't planning on meeting her or I probably wouldn't have worn my {adjective_2} {clothing}. I know most people would have bowed, but I forgot and decided to {verb} {adverb} instead. She smiled politely and then said, '{phrase_or_saying}.'""", "The Queen")

cooking_school = Story(["plural_noun_1", "adjective_1", "food", "color", "adjective_2", "phrase_or_saying", "plural_noun_2", "person", "number", "location"], """I just finished cooking school at {person}'s School of {adjective_1} {plural_noun_1}. The last day of classes, I wow-ed my teacher with a {color} {food} from {location}. I prepared it traditionally, so it was baked with {number} {plural_noun_2}. The instantly my teacher tried it, he exclaimed, '{phrase_or_saying}'. That's when I knew I would have a {adjective_2} career ahead of me!""", "Cooking School")