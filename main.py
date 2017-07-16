import praw
import config

######################
# Variables          #
######################
targetPhrase = 'Donald Trump'
responseString = 'You mean the orange guy on TV?'
######################

def signIn():
    r = praw.Reddit(client_id='CLIENT_ID',
                client_secret="CLIENT_SECRET",
                password='PASSWORD',
                user_agent='USERAGENT',
                username='USERNAME')
return r

def process_submission(submission):
    # Ignore titles with more than 10 words as they probably are not simple
    # questions.
    if len(submission.title.split()) > 10:
        return

    normalized_title = submission.title.lower()
    for question_phrase in QUESTIONS:
        if question_phrase in normalized_title:
            url_title = quote_plus(submission.title)
            reply_text = REPLY_TEMPLATE.format(url_title)
            print('Replying to: {}'.format(submission.title))
            submission.reply(reply_text)
            # A reply has been made so do not attempt to match other phrases.
            break


if __name__ == '__main__':
    main()

