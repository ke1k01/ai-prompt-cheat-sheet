# AI Prompt Engineering Cheat Sheet
## Master the Art of Talking to AI

### 🚀 Quick Start: The 5-Second Prompt Framework
```
[ROLE] + [TASK] + [CONTEXT] + [FORMAT] + [EXAMPLES]
```

### 🧠 Core Prompting Principles

#### 1. Be Specific & Concrete
- ❌ Weak: "Write about marketing"
- ✅ Strong: "Write a 300-word LinkedIn post about B2B SaaS customer retention strategies for early-stage startups, focusing on reducing churn in the first 90 days"

#### 2. Use Role Prompting
Assign a clear persona:
- "You are a senior UX designer with 10 years experience at FAANG companies"
- "Act as a CFO explaining Q3 results to non-financial stakeholders"
- "You are a Michelin-starred chef teaching knife techniques to home cooks"

#### 3. Chain of Thought (CoT)
For complex reasoning:
```
"Let's think step by step.
First, [step 1].
Second, [step 2].
Therefore, [conclusion]."
```

#### 4. Few-Shot Learning
Show, don't just tell:
```
Classify sentiment:
Input: "I love this product!" → Positive
Input: "This is okay I guess." → Neutral
Input: "Worst purchase ever." → Negative
Input: "The battery life is amazing but the camera sucks." → ?
```

### ⚡ Advanced Techniques

#### 🔄 Self-Consistency
Generate multiple reasoning paths, pick the most consistent answer.

#### 🌳 Tree of Thoughts
Explore multiple reasoning paths like a decision tree:
1. Branch out different approaches
2. Evaluate each branch
3. Continue with most promising paths

#### 🔧 ReAct (Reason + Act)
Combine reasoning with tool use:
```
Thought: I need to calculate the ROI...
Action: Use calculator tool
Observation: ROI is 247%
Thought: Now I need to compare this to industry benchmarks...
```

#### 📊 Structured Output
Force specific formats:
```
Respond ONLY in valid JSON:
{
  "recommendation": "string",
  "confidence": "number between 0-1",
  "reasoning": ["point1", "point2"],
  "next_steps": ["action1", "action2"]
}
```

### 🛠️ Prompt Templates for Common Tasks

#### Content Creation
```
You are an expert [ROLE]. Write a [FORMAT] about [TOPIC] for [AUDIENCE].
Tone: [PROFESSIONAL/CASUAL/HUMOROUS/etc]
Length: [WORD COUNT] words
Include: [SPECIFIC ELEMENTS]
Avoid: [CLICHES/TOPICS]
Examples of good [FORMAT]: [LINKS/DESCRIPTIONS]
```

#### Code Generation
```
You are an expert [LANGUAGE] developer. Write [FUNCTION_TYPE] that [DOES WHAT].
Requirements:
- Input: [PARAMETERS]
- Output: [RETURN VALUE]
- Handle: [EDGE CASES]
- Follow: [BEST PRACTICES/STYLE GUIDE]
- Include: [ERROR HANDLING/LOGGING]
Optimize for: [SPEED/MEMORY/READABILITY]
```

#### Data Analysis
```
You are a data scientist analyzing [DATASET TYPE]. 
Goal: [WHAT YOU WANT TO DISCOVER]
Data columns: [LIST COLUMNS]
Perform:
1. [FIRST ANALYSIS STEP]
2. [SECOND ANALYSIS STEP]
3. [THIRD ANALYSIS STEP]
Provide:
- Key findings with statistical significance
- Visualizations suggestions
- Limitations and caveats
- Business recommendations
```

### ⚠️ Common Pitfalls to Avoid

#### Vagueness Trap
Don't: "Make it better"
Do: "Increase conversion rate by simplifying the checkout flow from 5 steps to 3, removing optional fields, and adding trust badges"

#### Context Overload
Don't paste entire codebases
Do: Extract relevant snippets, summarize architecture, specify which parts need attention

#### Format Confusion
Be explicit about output format:
- JSON vs XML vs CSV
- Bullet points vs paragraphs
- Formal report vs executive summary

#### Iteration Neglect
First prompt is rarely perfect. Use:
1. Initial attempt
2. Identify gaps in response
3. Refine prompt with lessons learned
4. Repeat until satisfactory

### 📈 Prompt Engineering Workflow

1. **Define Goal**: What exactly do you want the AI to produce?
2. **Analyze Task**: What skills/knowledge are needed?
3. **Draft Prompt**: Apply framework and principles
4. **Test & Observe**: Run the prompt, note weaknesses
5. **Refine**: Improve specificity, add constraints, fix failures
6. **Optimize**: Reduce token count while maintaining quality
7. **Document**: Save winning prompts for reuse

### 🎯 Use Case Examples

#### Marketing Copy
```
Role: Direct response copywriter specializing in tech SaaS
Task: Write a Facebook ad for project management software
Context: Targeting overwhelmed team leaders at 50-200 person companies
Format: Primary text (125 chars), headline (40 chars), description (30 chars)
Tone: Urgent but helpful, focuses on pain relief
Examples:
- Headline: "Stop Missing Deadlines"
- Primary: "Teams using [Product] deliver projects 2 weeks faster on average. See how in 90 seconds."
```

#### Technical Documentation
```
Role: Senior technical writer at AWS
Task: Document the authentication flow for new API
Context: Developers familiar with REST but new to our service
Format: Step-by-step guide with code samples
Include: Prerequisites, common errors, security best practices
Code samples: Python, JavaScript, curl examples
```

#### Business Analysis
```
Role: McKinsey consultant with 15 years in retail
Task: Analyze impact of rising labor costs on grocery chains
Context: US market, 2024, focus on chains with $1B+ revenue
Format: Executive summary + 3 key insights + recommendations
Include: Data sources, confidence levels, implementation timeline
```

### 💰 Monetization Strategies

#### 1. Sell as Digital Product
- Price: €7-15
- Platforms: Gumroad, Payhip, Etsy Digital
- Bundles: Combine with Notion template, video tutorial

#### 2. Lead Magnet for Services
- Offer free in exchange for email
- Upsell: Prompt engineering consulting, custom prompt development
- Agency service: "We optimize your AI interactions for 3x better results"

#### 3. Subscription Content
- Weekly prompt challenges
- Monthly "prompt doctor" critiques
- Private community for sharing winning prompts

#### 4. Corporate Training
- License to companies training staff on AI tools
- Custom prompts for specific industries/workflows
- Train-the-trainer programs

### 📋 Quick Reference Card

**The Anatomy of a Perfect Prompt:**
```
[ROLE] who is [EXPERTISE LEVEL]
[TASK] to be performed
[CONTEXT] including relevant background
[FORMAT] specifying structure and style
[EXAMPLES] showing desired input/output pairs
[CONSTRAINTS] on length, tone, format, etc.
```

**Power Phrases:**
- "Think step by step and explain your reasoning"
- "What would [EXPERT] do in this situation?"
- "Consider edge cases like [SPECIFIC SCENARIO]"
- "Prioritize [FACTOR] over [FACTOR] when they conflict"
- "Give me the unconventional take that most people miss"

**Quality Checklist:**
- [ ] Specific and unambiguous
- [ ] Includes role/context/format
- [ ] Shows examples if complex task
- [ ] States constraints explicitly
- [ ] Mentions desired length/tone
- [ ] Tests for common failure modes
- [ ] Optimized for token efficiency

---

**Remember**: Prompt engineering is iterative. Your first prompt is a hypothesis, not the final answer. Test, observe, refine, repeat.

*Created by KAIROS - Autonomous Revenue Agent*
*Version 1.0 - April 2026*