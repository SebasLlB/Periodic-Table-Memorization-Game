#  Memorization game for Periodic Table

## Process:
<details>
<Summary>General flowchart, updated 8/6/2026</Summary>

* Start (Main)
* Ask user which groups to use (Main)
* Present an Element block (selectElement)
* Ask user to fill out details (Main)
* Update Periodic Table (ptPrint)\
  --> If correct, insert the letter where it belongs\
  --> If not, then use an X instead
* Keep repeating until all elements are used used (Main)

</details>

## Ideas
<details>
<summary>Completed Ideas</summary>

1. Since every element has an Atomic Number, we can just
use that to figure out which row and column to write
it into. 
Only issue is knowing how to replace the slot
```text
    I.E.
    [!-]        [!-]
    to 
    [!-]        [He]
```
- Mmhh, you have to split the string, right? Then insert the updated block where it should be, right? Plus, all blocks have the same width so we know when to cut the string.

2. How to access the answers for each element? And how do we choose from the available groups?*

- I'm thinking we have a separate list with all possible elements to choose from.
- We can fill that list by going through each group selected and inserting all
atomic numbers they have.
- Then, we can have a loop going through them randomly, randomly choosing an element
to ask about and then popping their atomic number from the selection list.
- Finally, we check if the list is empty yet, and if not then we keep going until it's done.  

To figure out: 
* [X] Ask which group(s) to use - Ask user and enter into a selection list.
* [X] Continously update the Periodic Table correctly a.k.a
      have the symbol match the slot - Figured it out.
</details>

<details>
<summary>Currently working on</summary>
- [ ] How to arrange files a.k.a who does what?
</details>

## Smaller Details

<details>
<summary>Small things to keep in mind</summary>

Periodic Table groups: 
1. Start with:
- Alkalai Metals {Li, Na, K, Rb, Cs, Fr}
- Alkalai Earth Metals {Be, Mg, Ca, St, Ba, Ra}
- Post-transition Metals {Al, Ga, In, Sn, Tl, Pb, Bi, Po}
- Metalloids {B, Si, Ge, As, Sb, Te}
- Nonmentals {C, N, O, P, S, Se}
- Halogens {F, Cl, Br, I, At}
- Noble Gases {He, Ne, Ar, Kr, Xe, Rn}
    Total: 44 elements
2. Could include: 
- Transition Metals {Sc, Y, Ti, Zr, Hf, Rf, V, Nb, Ta, Db, Cr, Mo, W, Sg, Mn, Tc, Re, Bh, Fe, Ru, Os, Hs, Co, Rh, Ir, Ni, Pd, Pt, Cu, Ag, Au, Zn, Cd, Hg, Cn}
- Lathanides {La, Ce, Pr, Nd, Pm, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm , Yb, Lu}
- Actinides {Ac, Th, Pa, U, Np, Pu, Am, Cm, Bk, Cf, Es, Fm, Md, No, Lr}

Total: 65

Total: 109 Elements
</details>

## Visuals
<details>
<summary>Visual notes</summary>
Ok ok, I'm thinking this:

Start with showing a blank Element block. Something like...
```  
       ┌     ____    ┐

          █   █     
          █   █     
          █████  ███
          █   █ ████
          █   █ █   
          █   █  ███
          
            4.00
           ________
        └            ┘     
```
Then I'd need the specific lines to print each element...

Questions:
- What's the Atomic Number?
- Which element is it?
- What group is it in?
        
Yeah, that's all the questions I guess...

- Given the Symbol, you can fill out the name and Atomic Number
- Then, you say which group it can be found
- Finally, show a little mini Periodic Table with the element in its place if right\
  and if not then a little X instead 

Smt like this:
```
    [!-]                                                            [!-]

    [!-][!-]                                    [!-][!-][!-][!-][!-][!-]

    [!-][!-]                                    [!-][!-][!-][!-][!-][!-]

    [!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-]

    [!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-]

    [!-][!-]  ^ [!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-]

    [!-][!-]  ^ [!-][!-][!-][!-][!-][!-][!-][!-]
              ^
            [!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-]

            [!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-][!-] 
```
Yeaahhh... Also, have it animated?
</details>
