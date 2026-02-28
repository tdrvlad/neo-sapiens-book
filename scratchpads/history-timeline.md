# History Timeline — Story of Computation

Events and milestones covered in the current draft of Chapter 2.

---

## Prehistoric

- **~20,000 BCE** — **Ishango Bone**: Baboon bone with deliberate notch patterns, interpreted as a counting mechanism. First evidence of humans abstracting quantities and generalizing through symbols.
- **Prehistoric (undated)** — **Tree carvings by hunter-gatherers**: Symbols carved at trail crossroads to mark paths, resources and dangers. First act of encoding environmental information into stable external symbols — a precursor to truth-bearing statements.

---

## Antiquity

- **~3000–2000 BCE** — **Egyptian practical geometry**: Rhind Mathematical Papyrus preserves rules for computing areas and volumes, including an approximation for the area of a circle. Geometry tied to land, labor, logistics.
- **~2000–1600 BCE** — **Old Babylonian scribes**: Clay tablets with sophisticated numerical procedures for managing fields, canals, taxation and trade. Mathematics as engineered recipe.
- **~1700 BCE** — **Hammurabi's Code**: First documented if-then-else logical structure applied to law. Demonstrates branching reasoning and anticipation of consequences.
- **~1700 BCE** — **Babylonian irrigation algorithms**: Step-by-step decision rules for managing canal and reservoir flow. First known algorithm: a defined sequence of conditional instructions to achieve a repeatable outcome.
- **~624–546 BCE** — **Thales of Miletus**: Shifts geometry from application to proof — seeks to show *why* relationships must hold, not just that they do.
- **~570–495 BCE** — **Pythagoras**: Advances the claim that number and proportion underlie the fabric of reality. Geometry as a window into necessity.
- **427–347 BCE** — **Plato**: Mathematical objects as ideal, perfect forms accessible only to reason. Geometry steps into abstract space.
- **~384–322 BCE** — **Aristotle**: Formalizes logic. Introduces the syllogism — a structure for deriving conclusions from premises. Truth becomes structural, not rhetorical.
- **~3rd–2nd c. BCE** — **The Stoics**: Extend Aristotle's logic. Identify the fundamental logical operators: **IF-THEN, AND, OR, NOT** — the building blocks of all computational logic.
- **~300 BCE** — **Euclid's *Elements***: Turns geometry into a model of deductive certainty. Nearly two thousand years of mathematical thinking flows from this.

---

## Medieval & Early Modern

- **Medieval period** — **Hindu-Arabic numeral system adopted in Europe**: Positional notation and the concept of zero transform calculation from specialist craft to scalable tool. Commerce, navigation, and administration drive demand.

---

## 17th Century

- **1642** — **Blaise Pascal — the Pascaline**: First mechanical calculator. Embeds arithmetic rules (including carry propagation) into physical gears. Demonstrates that calculation can be delegated to a machine.
- **~1670s** — **Gottfried Wilhelm Leibniz — Stepped Reckoner**: Extends Pascal's machine to perform multiplication via a stepped drum. First true calculator handling all basic arithmetic.
- **~1670s** — **Leibniz — binary numeral system**: Proposes a numerical system of only 1s and 0s, grounded in the metaphysical distinction between "something" and "nothing". Far ahead of its practical time.
- **~1670s** — **Leibniz — vision of a universal language of reasoning**: Envisions a symbolic calculus of thought in which all arguments could be resolved by calculation (*calculemus*).
- **1600s** — **William Gilbert**: Publishes rigorous study of magnetism. Declares Earth itself is a magnet — explains how compasses work. First systematic scientific account of electromagnetic phenomena.

---

## 18th Century

- **~1750s** — **Benjamin Franklin — kite experiment**: Demonstrates electricity is the force behind lightning. Foreshadows the possibility of harnessing electricity.
- **1794** — [SUGGESTION] **Claude Chappe — optical semaphore**: Shape-shifting signal tower that could be positioned into 92 distinct configurations (symbols). By sending *two consecutive* symbols, the system produced 92×92 = 8,464 unique combinations, vastly expanding the message space. Used a codebook: first symbol = page, second = entry on that page. First large-scale rapid long-distance communication system, first deployed militarily at the Battle of Fleurus. Establishes the key idea that *consecutive symbol selection multiplies the message space exponentially* — the conceptual seed of Hartley's information measure.
- **~1800** — **Alessandro Volta — first battery (voltaic pile)**: On-demand, controllable source of electricity. Enables systematic experimentation with electrical phenomena.
- **~1820** — **Hans Christian Ørsted**: Discovers that an electric current produces a magnetic field. Reveals the link between electricity and magnetism.
- **~1820s** — **First electric motor prototype**: Electricity converted into continuous mechanical motion. Reverse principle (motion → electricity) follows — energy becomes interchangeable and transferable over distance.

---

## 19th Century

- **1800s** — **Joseph Marie Jacquard — programmable loom**: Pattern designs encoded onto punched cards; the loom reads holes vs. solid positions (yes/no) to lift threads. First programmable machine: behavior changes depending on the instructions fed to it. Faces pushback from weavers fearing job loss.
- **1838 / 1844** — **Samuel Morse & Alfred Vail — telegraph and Morse code**: Information transmitted as electrical pulses over wire. Morse code maps letters to dot-dash patterns — a finite alphabet encoding arbitrary language. Binary signal (on/off) carries symbolic information across vast distances. [SUGGESTION] Crucially, Vail studied the *statistical frequency* of letters in English and assigned shorter codes to the most common ones (e.g. E = single dot) and longer codes to rare ones (e.g. Z). No mathematical theory backed this — pure intuition — but it was the first practical application of what Shannon would later formalise as entropy coding: matching code length to information content.
- **~1876** — [SUGGESTION] **Émile Baudot — Baudot code & teleprinter**: French engineer who automated telegraphy. Instead of Morse's variable-length codes, Baudot assigned every letter and number a *fixed 5-bit binary code* (32 possible values). Less efficient than Morse in theory (ignores letter frequency), but made full automation possible — a keyboard press mechanically impressed the five bits onto the line, and the receiver decoded them automatically. The direct ancestor of ASCII and all fixed-width digital character encodings. First system to treat text as a stream of uniform binary symbols.
- **~1847** — **George Boole — Boolean algebra** (*The Laws of Thought*, 1854): Treats logical statements as algebraic quantities with only two values (true/false, 1/0). Defines AND, OR, NOT as algebraic operations. Reasoning becomes manipulable like equations — a complete symbolic system for mechanical logic.
- **~1830s–1840s** — **Charles Babbage — Analytical Engine**: Programmable mechanical general-purpose computer (never completed). Equipped with memory, a processor, and conditional control — can execute abstract instructions, not just a fixed task.
- **~1880s** — **Herman Hollerith — punch card census system**: Adapts Jacquard's punch card idea to encode categorical data (age, occupation, region). Cards read mechanically for tabulation. Founding of what becomes IBM.
- **Late 19th century** — **Foundational crisis in mathematics**: Paradoxes in set theory (Russell, Cantor) reveal that logic itself may be unstable. The certainty of mathematics is thrown into doubt.

---

## Early 20th Century

- **Early 1900s** — **David Hilbert — formalization program & Entscheidungsproblem**: Proposes reducing all of mathematics to symbolic manipulation under explicit rules. Asks: does a general procedure exist to decide the truth of any mathematical statement?
- **~1920s** — [SUGGESTION] **Harry Nyquist — bandwidth and signaling rate**: Bell Labs engineer. Showed that the number of distinct symbols a channel can transmit per second is fundamentally limited by its *bandwidth* — the range of frequencies it can carry. Higher frequencies get stripped away as a signal travels; this distortion sets a hard ceiling on signaling speed. First to make the mathematical link between the continuous (analog) properties of a channel and the discrete (digital) symbols being sent through it. The Nyquist rate becomes a foundational constraint in all of information theory and digital communications.
- **1927** — [SUGGESTION] **Ralph Hartley — first quantitative measure of information**: Bell Labs. Presented at the International Congress of Telegraphy and Telephony (Lake Como, Italy). Proposed removing the "elastic" and subjective prior definitions of information and replacing them with a precise quantity. Key insight: when symbols are sent *consecutively*, the number of possible messages grows *exponentially* — each new symbol multiplies the total. Therefore, the sensible measure of information is the *logarithm* of the number of possible sequences (making it grow linearly with the number of selections). Hartley's measure: H = n × log(s), where s is the symbol alphabet size and n is the number of selections. Does not yet account for probability — treats all symbols as equally likely. The essential first step Shannon will complete two decades later.
- **1931** — **Kurt Gödel — incompleteness theorems**: Proves no sufficiently powerful formal system can be both complete and consistent. As a side effect: encodes logical statements as numbers, revealing that reasoning itself can be represented and processed symbolically.
- **1930s** — **Alonzo Church — lambda calculus**: Abstract formal system capturing the notion of computability in symbolic terms.
- **1936** — **Alan Turing — the Turing machine & universal computer**: Defines computation by abstracting what a human "computer" (clerk) does: read symbols, write symbols, shift states, follow rules. Realizes machine instructions can themselves be encoded as data — one machine can simulate any other. The concept of the general-purpose programmable computer is born.
- **1937** — [SUGGESTION] **Claude Shannon — master's thesis (MIT)**: Widely regarded as the greatest master's thesis in engineering history. Shannon showed that George Boole's algebra of logic (true/false, 1/0, AND/OR/NOT) could be directly implemented in *electrical switching circuits*. A logical proposition becomes a circuit; AND is switches in series; OR is switches in parallel; NOT is an inverter. This was the blueprint for digital electronics — the theoretical foundation of every computer chip ever built. Shannon was 21 years old.
- **1948** — [SUGGESTION] **Claude Shannon — information theory** (*A Mathematical Theory of Communication*): Published at Bell Labs. Built on Hartley's logarithmic measure but made one decisive advance: Hartley assumed all symbols equally likely. Shannon asked what happens when they are *not*. His answer: **entropy** — the average *surprise* of a source, weighted by probability. A certain outcome carries zero information; a rare outcome carries a lot. Key results: (1) **Source coding theorem**: any information source can be compressed down to its entropy — no further without losing information. (2) **Channel capacity**: every noisy channel has a maximum rate of reliable communication. (3) **Noisy channel theorem**: with the right coding, you can transmit at channel capacity with arbitrarily close to zero errors — even through a noisy channel. The **Shannon-Hartley theorem** (unifying Nyquist, Hartley, and Shannon) gives the capacity of a bandwidth-limited, noise-corrupted channel in a single equation. Shannon's framework becomes the foundation of data compression, cryptography, machine learning, and AI.

---

## Gaps / To Be Added

- Ada Lovelace (first programmer, notes on Babbage's Analytical Engine)
- Shannon's information theory ✓ (added as [SUGGESTION] from video transcript)
- Vacuum tubes and early electronic computers (ENIAC, Colossus, etc.)
- Transistor invention (Bell Labs, 1947)
- von Neumann architecture
- Early programming languages
- The path to modern computers through to early 2000s
