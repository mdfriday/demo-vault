---
title: "Google Analytics"
description: "Google Analytics is Google's free website analytics tool that tracks how people interact with your website and marketing campaigns."
date: 2026-10-02
tags:
  - seedling
---

## Definition

**Google Analytics** is Google's free website analytics tool that tracks how people interact with your website and marketing campaigns.

> [!CRITICAL]
> **Measurement is the foundation of optimization**
> 
> If you can't measure it, you can't improve it.

## Why Google Analytics Matters

### Strategic Importance

1. **Know Your Visitors**: Who comes to your site?
2. **Track Behavior**: What do they do on your site?
3. **Measure Conversions**: Are they taking desired actions?
4. **Identify Opportunities**: Where are the problems?
5. **Prove ROI**: Show results from marketing efforts
6. **Optimize Budget**: Double down on what works

## Module 1: Google Analytics Setup

### Installation

**Step 1**: Create Google Analytics Account
- Go to analytics.google.com
- Sign in with Google account
- Click "Create Account"

**Step 2**: Set Up Property
- Enter website name
- Select reporting timezone
- Currency settings

**Step 3**: Install Tracking Code
- Copy tracking ID
- Add to website (WordPress plugin: Google Site Kit)
- Verify installation (Analytics checks "Active for last 24 hours")

### Key Concepts

**Account** = Your organization (top level)
**Property** = Your website or app
**View** = Filtered version of data

**Best Practice**: Create filtered view to exclude internal traffic

## Module 2: Core Metrics & Navigation

### Main Dashboard Overview

| Section | Metrics Shown |
|---------|---------------|
| **Overview** | Users, sessions, bounce rate, session duration |
| **Audience** | Who visits (demographics, interests, devices) |
| **Acquisition** | Where visitors come from (traffic sources) |
| **Behavior** | What they do on site (pages viewed, time spent) |
| **Conversions** | Goals completed (tracked actions) |

### Understanding Key Metrics

#### Users
- Total unique visitors
- **Important for**: Understanding audience size
- **Optimization**: Increase through more marketing

#### Sessions
- Periods of user activity
- One user can have multiple sessions
- **30-minute inactivity ends session**
- **Important for**: Measuring engagement frequency
- **Target**: Users with high session frequency = loyal audience

#### Bounce Rate
- % of visitors who leave without any interaction
- **High bounce rate** (>50%) = Problem
  - Poor page content
  - Wrong traffic source
  - Slow load time
- **Optimization**: Improve page relevance

#### Session Duration
- Average time users spend on site
- **Higher = Better engagement**
- **Target**: 2+ minutes for content sites
- **Optimization**: Create engaging content, reduce friction

#### Pages Per Session
- Average # of pages viewed
- **Higher = Better engagement**
- **Low value**: Users not exploring site
- **Optimization**: Internal linking, navigation improvement

### Traffic Source Categories

| Source | Meaning | Examples |
|--------|---------|----------|
| **Organic** | Search engines | Google, Bing, Yahoo |
| **Direct** | Typed URL or bookmarks | yoursite.com |
| **Referral** | Links from other sites | Guest posts, reviews |
| **Social** | Social media traffic | Facebook, Twitter, LinkedIn |
| **Email** | Tracked email campaigns | Newsletter links |
| **Paid** | Paid advertising | Google Ads, Facebook Ads |
| **Display** | Banner ads | Adsense, display networks |

## Module 3: Conversion Tracking

### Setting Up Goals

> [!IMPORTANT]
> Without goal tracking, you're flying blind.
> 
> Define what "success" means for your business.

**Types of Goals**:
1. **Destination**: Reaching a page (thank you page)
2. **Event**: Specific action (button click, form submit)
3. **Duration**: Spending time on site
4. **Pages/Screens**: Viewing multiple pages

**Conversion Examples**:
- Email signup
- Product purchase
- Contact form submission
- Video watch
- Download
- Phone call

### Setting Up Conversion Tracking

**Step 1**: Define Goal
- Sales: Purchase completion
- Leads: Form submission or signup
- Engagement: Visited specific pages or time threshold

**Step 2**: Create in Analytics
- Admin → Goals → + Create Goal
- Choose goal type (Destination, Event, Duration, Pages)
- Set goal details
- Verify goal tracking

**Step 3**: Track in Ads
- Connect Google Ads to Analytics
- Conversions automatically tracked
- See ROI per ad/keyword

### E-Commerce Tracking

**For Online Stores**:
- Track product views
- Track add-to-cart
- Track purchases
- Calculate revenue per source

**Value**: Know exactly which marketing channels generate sales

## Module 4: Audience Analysis

### Demographic Data

**Who's visiting your site?**
- Age groups
- Gender
- Interests
- Device type (mobile, desktop, tablet)
- Geography

**Use Cases**:
- Is your marketing reaching the right people?
- Adjust marketing message to audience preferences
- Create more targeted campaigns

### Behavior Analysis

**What do they do?**

| Behavior | What It Shows |
|----------|--------------|
| **Returning Users** | % who visit again (loyalty indicator) |
| **User Type** | New vs Returning (repeat engagement) |
| **Device Category** | Mobile vs Desktop usage patterns |
| **Operating System** | iPhone vs Android users |
| **Browser** | Chrome, Safari, Firefox compatibility |

**Optimization**:
- High mobile traffic? Ensure mobile optimization
- High returning users? Build loyalty programs
- Low repeat visits? Improve content quality

## Module 5: Traffic Analysis (Acquisition)

### Analyzing Each Traffic Source

#### Organic Traffic (SEO)
- **Metric**: Organic sessions
- **Optimization**: More keywords ranking, more content
- **Benchmark**: 30%+ of total traffic = healthy
- **Keyword Report**: See which keywords drive traffic

#### Direct Traffic
- **Metric**: Direct sessions
- **Meaning**: Bookmarks, typed URL, email
- **Optimization**: Build brand awareness so people come back

#### Referral Traffic
- **Metric**: Referral sessions
- **Meaning**: Links from other websites
- **Optimization**: Guest posting, partnerships

#### Social Media Traffic
- **Metric**: Social sessions
- **By Platform**: See which social channel drives most traffic
- **Optimization**: Focus effort on top performing platform

#### Email Traffic
- **Metric**: Email campaigns → sessions
- **Optimization**: Test different send times, subject lines

#### Paid Ads Traffic
- **Metric**: Campaign performance
- **ROI**: Sessions × Conversion Rate × Order Value
- **Optimization**: Scale winning campaigns, pause losers

## Module 6: Setting Up a Review Rhythm

### Monthly Review Process

**Step 1**: Schedule Monthly Review
- Last day of month, 1 hour
- Block calendar time
- Gather stakeholders

**Step 2**: Prepare Dashboard
- Create custom dashboard with key metrics
- Compare to previous months
- Note significant changes

**Step 3**: Analyze Results
- What traffic sources performed best?
- What pages converted best?
- What campaigns had best ROI?
- What problems emerged?

**Step 4**: Document Insights
- Top 3 wins
- Top 3 problems
- 3 optimizations for next month

**Step 5**: Take Action
- Implement changes
- Double down on what works
- Fix what's broken

### Weekly Email Reporting

**Setup**: 
- Create custom email report
- Admin → Reporting → Email Reports
- Schedule weekly delivery
- Include key metrics

**Review**: 
- 5-minute weekly scan
- Spot trends early
- Catch problems quick

### Real-Time Alerts

**Setup**: 
- Admin → Alerts
- Create alert for unusual traffic spikes
- Alert if traffic drops
- Alert if conversions increase

**Use Case**: 
- Ad campaign launches → Monitor in real-time
- Website issues → See traffic drop immediately
- Viral content → Capture the moment

## Module 7: Google Analytics Optimization Workflow

### Week 1-2: Baseline

**Activities**:
- Install analytics tracking
- Set up 5-10 goals
- Create custom dashboard
- Analyze past month

**Deliverable**: Baseline metrics established

### Week 3-4: Optimization Starts

**Activities**:
- Improve top traffic-driving pages
- Test changes
- Monitor conversion rate
- Document A/B tests

**Metrics to Track**:
- Bounce rate of top pages
- Time on page
- Conversion rate by source
- Cost per acquisition (paid campaigns)

### Month 2+: Continuous Improvement

**Ongoing**:
- Monthly review meetings
- Weekly email reports
- Real-time alerts
- Test and iterate
- Scale winners, pause losers

## Assignment: Analytics Mastery

## Practice

Set up comprehensive analytics:

- [ ] Install Google Analytics on website
- [ ] Verify tracking is working
- [ ] Set up 5-10 goals (relevant to business)
- [ ] Create custom dashboard
- [ ] Set up demographic reports
- [ ] Analyze traffic sources
- [ ] Identify top performing content
- [ ] Connect Google Ads account
- [ ] Set up e-commerce tracking (if applicable)
- [ ] Create custom email report
- [ ] Set up real-time alerts
- [ ] Schedule monthly review meetings
- [ ] Document 5 optimization opportunities
- [ ] Implement 3 changes based on data


## Quick Reference: Knowledge Checklist

- [ ] Google Analytics: Free, essential measurement tool
- [ ] Track everything: Users, behavior, conversions
- [ ] Bounce rate > 50% signals problem
- [ ] Session duration measures engagement
- [ ] Goal tracking is non-negotiable
- [ ] Multiple traffic sources reduce dependency
- [ ] Organic traffic is most valuable (free)
- [ ] Monthly reviews catch trends
- [ ] Weekly email reports enable quick decisions
- [ ] Real-time alerts catch opportunities immediately
- [ ] Test one change at a time (measure impact)
- [ ] Double down on high-ROI channels
- [ ] Pause low-performing campaigns
- [ ] Measurement enables optimization

## Related Modules

[[01-Digital-Marketing-Strategy]] | [[07-SEO]] | [[08-YouTube-Marketing]] | [[13-Google-AdWords]]

**For Complete Analytics System**: See [[Google Analytics/index|Google Analytics Knowledge Base]] (6 detailed articles):
- Setup and installation
- Views, filters, and data foundations
- Goals, events, and conversion tracking
- Audience, behavior, and acquisition reports
- Segments, dashboards, and alerts
- Spam cleanup and platform integration

---

**Key Takeaway**: Data-driven decisions beat guesses. Install analytics, set goals, and review monthly. Your optimization roadmap is hidden in your analytics.
