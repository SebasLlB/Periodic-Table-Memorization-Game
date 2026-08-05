'''
    Idea: Memorization game for Periodic Table

    * Start: 
    * Present an Element block
    * Ask user to fill out details
    * Update Periodic Table
    * If correct, insert the letter where it belongs
    * If not, then use an X instead
    
    To figure out:
    * Ask which group(s) to use
    * Continously update the Periodic Table correctly a.k.a
      have the symbol match the slot

    Ideas:
    * Since every element has an Atomic Number, we can just
      use that to figure out which row and column to write
      it into. 
      Only issue is knowing how to replace the slot

      I.E.
      [!-]        [!-]
      to 
      [!-]        [He]

      Mmhh, you have to split the string, right?
      Then insert the updated block where it should be, right?
      Plus, all blocks have the same width so we know when to cut
'''