"""
example input:
noun: dog
verb: walk
adjective: blue
adverb: quickly

example output:
'Do you walk your blue dog quickly? That's hilarious!'
"""
from dataclasses import dataclass
from random import choice

interjections = [
    "Ah, I don't know if that's true.",
    "Aha! I figured it out!",
    "Ahem, could you boys stop talking so we could get on with class, please?",
    "Alas, it was not to be.",
    "Amen, hallelujah, amen!",
    "Aw, do we have to?",
    "You two are dating? Awesome!",
    "Aww, that's so cute!",
    "Bah, humbug!",
    "Oh, baloney. I don't believe that.",
    "Big  Big deal. Who cares?",
    "Bingo! Right on target!",
    "Boo! Scared you!",
    "Boo- That makes me sad. Boo-hoo.",
    "Brilliant, luv, absolutely brilliant!",
    "Oh, wow, that is so cool!",
    "Cowabunga, dude!",
    "Dang it! Where'd I put that?",
    "Well, duh. I can't believe you didn't know that.",
    "Eh? What?",
    "Enjoy! I hope you like it!",
    "Party time, excellent!",
    "Fabulous! That's just wonderful!",
    "Fantastic! I just love it!",
    "Finally! I never thought that'd be done.",
    "Freeze! Stop right there!",
    "Golly",
    "Good heavens! How did that happen?",
    "Whatever I feel like I wanna do, gosh!",
    "Great! I'm so excited you'll come along!",
    "Ha-ha! That's funny!",
    "Glory be to God, hallelujah!",
    "Heavens",
    "Holy mackerel",
    "Hooray!",
    "Huh. I have no idea.",
    "Ick! How gross!",
    "Indeed! I'll bet you didn't know that!",
    "Jeez, do we really have to go through this now?",
    "Kaboom! It blew up!",
    "Man, that's unbelievable.",
    "Marvelous! Oh, honey, that's just wonderful.",
    "My! I never once thought of it, Huck!",
    "My goodness my heavens, my stars, my word: My  isn't that just grand?",
    "Nah, it'll never work.",
    "No thank you. No problem.",
    "No way!",
    "Nope. I can't do that.",
    "Nuts! I wish I didn't have to.",
    "Oh boy",
    "Oh dear,",
    "oh my, ",
    "oh my gosh, ",
    "oh my goodness, ",
    "oh no!",
    "Oh! That's shocking!",
    "OK",
    "Shh! Quiet in the library!",
    "Super! That's fantastic!",
    "Swell! How great!",
    "Well, I just don't know about that.",
    "Woo-hoo! That's fantastic!",
    "Wow! I love it!",
    "Yabba dabba doo!",
    "Yippie! That's exciting!",
    "Yummy! I love chocolate cake!",
]


@dataclass
class MadLibInput:
    noun: str
    verb: str
    adjective: str
    adverb: str


@dataclass
class Response:
    output: str


def make_mad_lib(input: MadLibInput) -> Response:
    response = Response(
        output=f"So the {input.adjective} {input.noun} {input.verb} {input.adverb},"
    )
    return response


if __name__ == "__main__":
    print("madlibs!")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter a adjective: ")
    adverb = input("Enter a adverb: ")
    input = MadLibInput(
        noun=noun,
        verb=verb,
        adjective=adjective,
        adverb=adverb,
    )
    response = make_mad_lib(input)
    print(response.output, choice(interjections))
