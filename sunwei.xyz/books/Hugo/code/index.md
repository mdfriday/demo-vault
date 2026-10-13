---
weight: 1
title: "Deep Dive into Hugo: Source Code Analysis and Implementation Principles"
---

# Source code — read more, and read the good books

Learning has stages: understand, know, and can do.
If I follow someone else's explanation and it makes sense, I understand it.
If I can also retell it, I know it.
If I know it, can practice it, and the result is decent, then I can do it.

Take writing as an example.
After reading an article about writing, I understand that writing is recording my own ideas. That is understanding what writing is.
After thinking it through, I can retell that article and explain to someone else what writing is. That is knowing.
Then I start practicing from that understanding and fully express my own ideas. Then I can say I can write.

Reading source code is the same.
I want to learn, by reading source code, how a good open-source project works, to know the principles, and to turn what I absorb into the ability to do the work myself.

Everyone knows we should read more, especially good books.
Excellent source code is like a good book. So many excellent open-source projects are sitting there, within reach. Why do so few people read them?

I think there are two main reasons:
* The amount of code is huge, and it is not clear where to start. A good open-source project is usually large. Without someone to lead you in, doing it alone is hard.
* Programming languages were designed to be written, not to be read.
  Natural language is mainly for communication, between people.
  A programming language is between a person and a machine. An engineer expresses an idea in code the computer can understand, so the machine can carry out the instruction.

**How to explore**

To get a real grasp of Hugo in the site domain, I will study the Hugo source in these steps, until I can do it:

1. Small steps. Start from source that runs. Learn it in pieces. Stay on the current module, keep the load down, and check guesses against the source as it runs.
2. See it clearly. Unfold the source layer by layer with sequence diagrams, and understand the flow and the design details.
3. Abstract and summarize. Use the von Neumann frame — Input -> [?] -> Output — to summarize how it is implemented, which helps understanding and summary.
4. Practice. Diagram the key design points and get the essence. Explain the source with the source, spell out the basics, and make them solid.
