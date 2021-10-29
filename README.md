# Questions
### Please explain Big-O notation in simple terms.
I had not actually been familiar with this term until now. After looking into it, it appears to essentially be a way of describing an algorithm's efficiency. Attempting to apply the idea to VFX, imagine you rendered an identical scene from two different computers - one which is blazing fast while the other should be put out to pasture. When comparing each image's convergence graphs (number of samples x number of pixels converged), both of them should have similarly appearing function curves, relative to one another. A scene will have the same render convergence complexity, or the same "Big-O", regardless of the machine it's run on.

### What are the most important things to look for when reviewing another team member's code?
* Legibility - It should be easy to read/understand and have a general flow to it.
* Conciseness - Code should be as brief as allowable while maintaining comprehensibility.
* Documentation - Docstrings allow others to understand the general purpose of the code. Comments can help a lot, too.
* Consistency - Stylistically, it should "fit in" with the rest of the codebase/repo/file.
* If the author of the code disappeared tomorrow, how screwed would we be?

### Describe a recent interaction with someone who was non-technical. What did you need to communicate and how did you do it?
I somewhat recently described to a Project Manager how assets get imported into a Katana scene, given our pipeline. I needed to communicate the concept of an "importer delegate", which is code that is responsible for processing specific types of assets (camera, layout, animation, etc). I seemed to have been successful when using an example of a playground sieve. You load up the sieve with sand and when you lift it up, particles of sand which are smaller than that of the playground sieve's "mesh" will pass through, unobstructed, leaving behind larger objects (like rocks). Importer delegates work the same way with assets. If a given asset does not meet certain criteria it will not to be processed by the current delegate and will be passed on to the next delegate type.

I am of the belief that when you are attempting to explain something technical to a non-technical person, you have to be able to anchor the concept to something they know already. This allows them to have some frame of reference to lean on as the concept is unfolding to them.

Thinking about it now, I wonder if a litterbox scoop would have been a better example...

### Priority Queuer
