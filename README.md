# Subscriber-Checker

Are you willing to add **force-subscribe option** in all your telegram bots, but tired of adding bots to your channel?

Just use one API for all your bots.

- Demo API https://member-checker.vercel.app
- Bot [@BRMemberChecker_Bot](https://telegram.dog/BRMemberChecker_Bot)


### Demo Usage
```python
import requests
print(
    requests.get(
        "https://member-checker.vercel.app",
        params = {
            "chat_id": CHANNEL_ID,
            "user_id": MEMBER_ID,
        }
    ).json()
)
```

### Note
Only IDs are supported so that it doesn't raise FLOODWAIT.

Yes, you have to add this bot in your channel (without any admin rights ofcourse).


### Deploy on vercel
`BOT_TOKEN` is required.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fbuddhhu%2FMember-Checker&env=BOT_TOKEN)

**Enjoy coding 👨‍💻**
