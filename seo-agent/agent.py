#!/usr/bin/env python3
"""
SEO Agent for SB Margan Roofing
Usage:
  python agent.py content --service "flat roofing" --location "Birmingham"
  python agent.py keywords --service "guttering" --location "Quinton"
  python agent.py gmb-post --service "roof repair" --location "Harborne"
  python agent.py meta --page "flat roofing birmingham"
  python agent.py blog --topic "winter roof maintenance tips birmingham"
  python agent.py review-response --rating 5 --reviewer "John" --context "flat roof extension"
"""

import argparse
import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

try:
    from openai import OpenAI
except ImportError:
    print("\033[91mError: openai package not installed. Run: pip install -r requirements.txt\033[0m")
    sys.exit(1)

# ─────────────────────────────────────────
# ANSI colours
# ─────────────────────────────────────────
RESET  = "\033[0m"
BOLD   = "\033[1m"
CYAN   = "\033[96m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
ORANGE = "\033[38;5;208m"
RED    = "\033[91m"
GREY   = "\033[90m"


def banner():
    print(f"""
{ORANGE}{BOLD}  ___  ___     __  __                             {RESET}
{ORANGE}{BOLD} / __|| _ )   |  \/  | __ _  _ _  __ _  __ _ _ _  {RESET}
{ORANGE}{BOLD} \\__ \\| _ \\   | |\/| |/ _` || '_|/ _` |/ _` | ' \ {RESET}
{ORANGE}{BOLD} |___/|___/   |_|  |_|\\__,_||_|  \\__, |\\__,_|_||_|{RESET}
{ORANGE}{BOLD}                                  |___/  Roofing SEO {RESET}
{GREY}  AI-powered SEO content generator for sbmarganroofing.uk{RESET}
""")


# ─────────────────────────────────────────
# Business context injected into every prompt
# ─────────────────────────────────────────
BUSINESS_CONTEXT = """
Business: SB Margan Roofing
Owner: Sergiu Margan
Phone: 07580 085 430
Email: sergiumargan@yahoo.com
Address: 121 Merritts Hill, Birmingham B31 1PA
Website: https://sbmarganroofing.uk/
Service areas: Birmingham, Quinton, Northfield, Halesowen, Harborne, Selly Oak, Bromsgrove, Droitwich
Services: Flat Roofing (GRP fibreglass, EPDM rubber, felt), Tiled & Slated Roofs (clay, concrete, natural slate),
  Guttering & Fascias (UPVC), Chimney & Leadwork, general roof repairs, emergency roofing
Key USPs: 15+ years experience, owner-operated (Sergiu does every job personally), no subcontractors,
  no pushy salespeople, fully insured, written guarantees, free surveys, no hidden costs
Tone: Honest, plain-spoken, professional, local, trustworthy. Never hypey or salesy.
"""

MODEL = "gpt-4o-mini"


def get_client():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print(f"{RED}Error: OPENAI_API_KEY environment variable not set.{RESET}")
        print(f"{GREY}Set it with: export OPENAI_API_KEY=sk-...{RESET}")
        sys.exit(1)
    return OpenAI(api_key=api_key)


def call_openai(client, system_prompt, user_prompt):
    """Call OpenAI chat completion and return the result text."""
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": user_prompt},
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"{RED}OpenAI API error: {e}{RESET}")
        sys.exit(1)


def save_output(text, filepath):
    """Save text output to a file."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"\n{GREEN}Saved to: {filepath}{RESET}")


def print_result(label, text):
    print(f"\n{CYAN}{BOLD}{'─' * 60}{RESET}")
    print(f"{ORANGE}{BOLD}{label}{RESET}")
    print(f"{CYAN}{'─' * 60}{RESET}\n")
    print(text)
    print(f"\n{CYAN}{'─' * 60}{RESET}")


# ─────────────────────────────────────────
# COMMAND: content
# ─────────────────────────────────────────
def cmd_content(args, client):
    """Generate on-page SEO content for a service + location combination."""
    system = f"""You are an expert SEO copywriter specialising in local UK trades businesses.
You write for the following business:
{BUSINESS_CONTEXT}
Write content that is genuinely useful, reads naturally, and is optimised for local search.
Target 500-700 words. Use H2 headings. No markdown code fences. Include the location and
service in the first paragraph. End with a clear call to action mentioning the phone number.
"""
    user = f"Write an SEO-optimised web page section for the service '{args.service}' targeting the location '{args.location}' for SB Margan Roofing."
    result = call_openai(client, system, user)
    print_result(f"SEO CONTENT: {args.service.title()} in {args.location.title()}", result)
    if args.output:
        save_output(result, args.output)


# ─────────────────────────────────────────
# COMMAND: keywords
# ─────────────────────────────────────────
def cmd_keywords(args, client):
    """Generate a keyword research list for a service + location."""
    system = f"""You are a local SEO specialist for UK trades businesses.
Business context:
{BUSINESS_CONTEXT}
Provide keyword research output in a clean, structured format.
"""
    user = f"""Generate a comprehensive local SEO keyword list for '{args.service}' targeting '{args.location}'.
Include:
1. Primary keywords (high intent, exact-match local)
2. Secondary keywords (related services, nearby areas)
3. Long-tail keywords (questions, problem-based)
4. Negative keywords to avoid
For each keyword estimate relative search intent (high/medium/low) and competition (high/medium/low).
Format as a clean list, ready to paste into a keyword tracking spreadsheet."""
    result = call_openai(client, system, user)
    print_result(f"KEYWORDS: {args.service.title()} | {args.location.title()}", result)
    if args.output:
        save_output(result, args.output)


# ─────────────────────────────────────────
# COMMAND: gmb-post
# ─────────────────────────────────────────
def cmd_gmb_post(args, client):
    """Generate a Google Business Profile post."""
    system = f"""You are a social media and local SEO specialist for UK trades businesses.
Business context:
{BUSINESS_CONTEXT}
Write Google Business Profile posts that are concise (150-300 words), engaging,
include a clear call to action, mention the phone number, and feel local and authentic.
Avoid corporate-speak. Write in the voice of Sergiu, a real person who does the work himself.
"""
    user = f"Write a Google Business Profile post about '{args.service}' for customers in '{args.location}'. Make it feel real and local, not like an advert."
    result = call_openai(client, system, user)
    print_result(f"GMB POST: {args.service.title()} | {args.location.title()}", result)
    if args.output:
        save_output(result, args.output)


# ─────────────────────────────────────────
# COMMAND: meta
# ─────────────────────────────────────────
def cmd_meta(args, client):
    """Generate SEO meta title and description."""
    system = f"""You are an SEO specialist for a UK roofing company.
Business context:
{BUSINESS_CONTEXT}
Write meta titles and descriptions that are optimised for click-through rate and local search.
Meta title: max 60 characters. Meta description: max 155 characters.
Always include the business name and location. Output both clearly labelled.
"""
    user = f"Generate an SEO meta title and meta description for the page: '{args.page}' for SB Margan Roofing."
    result = call_openai(client, system, user)
    print_result(f"META TAGS: {args.page.title()}", result)
    if args.output:
        save_output(result, args.output)


# ─────────────────────────────────────────
# COMMAND: blog
# ─────────────────────────────────────────
def cmd_blog(args, client):
    """Generate a full blog post."""
    system = f"""You are a content writer for a UK roofing company blog.
Business context:
{BUSINESS_CONTEXT}
Write helpful, informative blog posts aimed at homeowners in Birmingham and the West Midlands.
Target 700-1000 words. Use H2 and H3 subheadings. Include practical advice. Write in a plain,
trusted voice. Include 2-3 internal link suggestions (just indicate [LINK TO: page]) where relevant.
End with a brief call to action and the phone number.
"""
    user = f"Write a blog post on the topic: '{args.topic}'"
    result = call_openai(client, system, user)
    print_result(f"BLOG POST: {args.topic.title()}", result)
    if args.output:
        save_output(result, args.output)


# ─────────────────────────────────────────
# COMMAND: review-response
# ─────────────────────────────────────────
def cmd_review_response(args, client):
    """Generate a professional response to a customer review."""
    system = f"""You are writing review responses for a small UK roofing business.
Business context:
{BUSINESS_CONTEXT}
Responses should:
- Thank the reviewer by name
- Acknowledge specific details mentioned
- Be warm, personal and genuine (written as Sergiu, the owner)
- For 5-star reviews: briefly mention another service or area for SEO
- For negative reviews: apologise genuinely, take responsibility, offer to resolve offline
- Keep responses to 80-120 words
- Never be sycophantic or use hollow phrases like 'We value your feedback'
"""
    stars = "★" * args.rating + "☆" * (5 - args.rating)
    user = f"Write a response to a {args.rating}-star review ({stars}) from a customer named '{args.reviewer}'. Context about their experience: '{args.context}'"
    result = call_openai(client, system, user)
    print_result(f"REVIEW RESPONSE: {args.rating}★ from {args.reviewer}", result)
    if args.output:
        save_output(result, args.output)


# ─────────────────────────────────────────
# CLI SETUP
# ─────────────────────────────────────────
def main():
    banner()

    parser = argparse.ArgumentParser(
        description="SB Margan Roofing SEO Agent - AI-powered content generation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python agent.py content --service "flat roofing" --location "Birmingham"
  python agent.py keywords --service "guttering" --location "Quinton"
  python agent.py gmb-post --service "roof repair" --location "Harborne"
  python agent.py meta --page "flat roofing birmingham"
  python agent.py blog --topic "winter roof maintenance tips birmingham"
  python agent.py review-response --rating 5 --reviewer "John" --context "flat roof extension"

Output to file:
  python agent.py blog --topic "winter tips" --output output/blog-winter.txt
        """
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # content
    p_content = subparsers.add_parser("content", help="Generate on-page SEO content")
    p_content.add_argument("--service", required=True, help="e.g. 'flat roofing'")
    p_content.add_argument("--location", required=True, help="e.g. 'Birmingham'")
    p_content.add_argument("--output", help="Save output to file path")

    # keywords
    p_keywords = subparsers.add_parser("keywords", help="Generate local SEO keyword list")
    p_keywords.add_argument("--service", required=True, help="e.g. 'guttering'")
    p_keywords.add_argument("--location", required=True, help="e.g. 'Quinton'")
    p_keywords.add_argument("--output", help="Save output to file path")

    # gmb-post
    p_gmb = subparsers.add_parser("gmb-post", help="Generate a Google Business Profile post")
    p_gmb.add_argument("--service", required=True, help="e.g. 'roof repair'")
    p_gmb.add_argument("--location", required=True, help="e.g. 'Harborne'")
    p_gmb.add_argument("--output", help="Save output to file path")

    # meta
    p_meta = subparsers.add_parser("meta", help="Generate meta title and description")
    p_meta.add_argument("--page", required=True, help="e.g. 'flat roofing birmingham'")
    p_meta.add_argument("--output", help="Save output to file path")

    # blog
    p_blog = subparsers.add_parser("blog", help="Generate a full blog post")
    p_blog.add_argument("--topic", required=True, help="e.g. 'winter roof maintenance tips birmingham'")
    p_blog.add_argument("--output", help="Save output to file path")

    # review-response
    p_review = subparsers.add_parser("review-response", help="Generate a review response")
    p_review.add_argument("--rating", required=True, type=int, choices=range(1, 6), help="Star rating 1-5")
    p_review.add_argument("--reviewer", required=True, help="Reviewer's name")
    p_review.add_argument("--context", required=True, help="Context about the job or review")
    p_review.add_argument("--output", help="Save output to file path")

    args = parser.parse_args()
    client = get_client()

    dispatch = {
        "content":         cmd_content,
        "keywords":        cmd_keywords,
        "gmb-post":        cmd_gmb_post,
        "meta":            cmd_meta,
        "blog":            cmd_blog,
        "review-response": cmd_review_response,
    }

    dispatch[args.command](args, client)


if __name__ == "__main__":
    main()
