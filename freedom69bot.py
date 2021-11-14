
## Twitter API keys

# Access keys - third regenerate in app settings
ACCESS_TOKEN = ""
ACCESS_SECRET = ""

# Consumer keys - first regenerate in app settings
APP_TOKEN = ""
APP_SECRET = ""

## DeepAI API key
AI_KEY = ""

errCount = 0
def main(args):
    print(".", end="")
    # Funny messages
    join = ("",
            ", verified by EidamGD",
            " and amogus",
            ", the perfect Geometry Dash level",
            " is the peak of CSGD",
            " is a megacollab",
            " funny")
    
    while True:
        # DeepAI request
        data = {"text":"Freedom69"+random.choice(join)}
        headers={'api-key': AI_KEY}
        generator = requests.post("https://api.deepai.org/api/text-generator",data,headers=headers)
        
        story = generator.json()["output"][:280]
        
        # Parsing the result (making sure it can fit in a tweet!!)
        fstopCount = story.count(".")
        if fstopCount == 0:
            story = story[:277]+"..."
        
        lastSentence = story.replace(".","%",fstopCount-1)
        cutoff = story[:lastSentence.index(".")+1]
        
        # Sending tweet
        try:
            print(".", end="")
            # Auto-translation to Czech. Only send cutoff if you don't want translation!
            t.statuses.update(status=translators.google(cutoff,from_language="en", to_language="cs").replace("Svoboda69","Freedom69"))
            print("Tweet sent!")
            break
        except Exception as twitError:
            if errCount == 3:
                print("Max error count reached!")
                break
            
            errCount += 1
            print("Error: "+twitError)
            continue
    
    return 0

if __name__ == '__main__':
    import sys, requests, os, random, translators, twitter
    
    # Logging into Twitter
    print("Sending.", end="")
    t = twitter.Twitter(auth=twitter.OAuth(ACCESS_TOKEN,ACCESS_SECRET,APP_TOKEN,APP_SECRET))
    
    sys.exit(main(sys.argv))
