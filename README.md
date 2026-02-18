# Authentication Tinker
This project is simply me tinkering and (re)learning Basic Authentication, Bearer Authentication, and JWTs. I'm 
interested in both what the backend and frontend code will look like. I'm also interested in providing a means to
tinker interactively where useful (like messing with JWTs). I'll be skipping HTTPS for simplicity as not intended
to be a production setup. I'll also be skipping a DB query and hardcoding that data as well in the server.

## Note about AI:
Since it's 2026 and no one will be doing code completely by hand going forward (short probably for a challenge or due
to a hard requirement), I'll be using Grok, and possibly Codeium, for initial boilerplate examples and retool from 
there as needed.

## Signing Algos:
- HS256 = HMAC SHA-256 (1-key system).
- RS256 = RSA SHA-256 (2-key system).

## Initial plan:
1. Hack together a quick python webserver.
   1. Monitor output.
   2. Backend auth code as needed.
   3. Provide API endpoints.
2. Hack together a quick client script.
   1. In place of a browser.
   2. Manual sending of headers, etc.
   3. Add interaction later (like with _Click). Start with hard coding.
3. Implement Basic Authentication.
   1. i.e. UN + PW over HTTPS.
4. Implement Bearer Authentication.
   1. Opaque Bearer Token.
   2. JWT Bearer Token.
5. Implement Authentication w/JWTs.
   1. One Token Strategy (Access Token).
   2. Two Token Strategy (Access + Refresh Token).
