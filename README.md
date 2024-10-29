# Brainrot Programming Language Specification

⚠️ not finished, but the examples are working in linux ⚠️

---

### Linux set up
```brainrot
git clone https://github.com/mmtmn/brainrot;cd brainrot;sudo ./setup_linux
```
---

#### **Run an example**

```brainrot
cd brainrot; cd examples
bruh hello_world.brot
```

---
flex: print

yap: comment

beta: mutable variable

sigma: immutable variable


# Data types

vibe: boolean

stack: integer

sauce: double

quote: string

squad: array

facts: dictionary


# Conditional statements

vibe check: if

bro did not pass: else


# Loops

bussin': while

hits different: break

hot take: continue

body count: loop iteration variable name (best practice)


# Functions

main character: main function

dms: function

slide into dms: function call

slide back: return

understood the assignment: program completed successfully / return 0


# Input/Output

flex: print

left on read: user input


# Operators

drip: +

lack: -

combo: *

ratio: /

no cap: ==

cap: !=


# Classes

squad goals: class

blud: friend class

highkey: public member

lowkey: private member

guarded af: protected member

cook: create an instance

cooked: deallocate an instance


# Exceptions

yeet: throw

red flag: error

send it: try

caught in 4k: catch

last chance bro: finally


---


#### **Output**

- **Print:** `flex`
  ```brainrot
  flex "This will show up on your terminal"
  ```

---

#### **Comment Syntax**
- **Keyword:** `yap`
- **Example:** 
  ```brainrot
  yap This is a comment and will not show up on your terminal
  ```

---

#### **Variables**

- **Mutable Variable:** `beta`
  ```brainrot
  beta age stack = 25
  ```
- **Immutable Variable:** `sigma`
  ```brainrot
  sigma pi sauce = 3.14
  ```

---

#### **Data Types**

- **vibe**: Boolean
  ```brainrot
  beta is_active vibe = true
  ```
- **stack**: Integer
  ```brainrot
  beta score stack = 100
  ```
- **sauce**: Double
  ```brainrot
  beta price sauce = 19.99
  ```
- **quote**: String
  ```brainrot
  sigma greeting quote = "Hello, world!"
  ```
- **squad**: Array
  ```brainrot
  beta numbers squad = [1, 2, 3]
  ```
- **facts**: Dictionary
  ```brainrot
  beta person facts = {"name": "John", "age": 30}
  ```

---

#### **Conditional Statements**

- **If:** `vibe check`
- **Else:** `bro did not pass`
  ```brainrot
  vibe check (age no cap 21) {
      flex "You can enter the club"
  } bro did not pass {
      flex "You're too young for this"
  }
  ```

---

#### **Loops**

- **While Loop:** `bussin'`
- **Break:** `hits different`
- **Continue:** `hot take`
- **Iteration Variable (Best Practice):** `body count`
  ```brainrot
  beta body count stack = 0
  bussin' (body count < 5) {
      flex "Looping..."
      body count drip= 1
      vibe check (body count no cap 3) {
          hits different
      }
  }
  ```

---

#### **Functions**

- **Main Function:** `main character`
- **Define Function:** `dms`
- **Function Call:** `slide into dms`
- **Return Value:** `slide back`
  ```brainrot
  dms add stack x stack y {
      slide back x drip y
  }

  main character {
      beta result stack = slide into dms add 10 20
      flex result
      understood the assignment
  }
  ```

---

#### **Input/Output**

- **Print:** `flex`
  ```brainrot
  flex "Hello, Brainrot!"
  ```
- **User Input:** `left on read`
  ```brainrot
  beta user_name quote = left on read "What's your name? "
  flex "Welcome, " drip user_name
  ```

---

#### **Operators**

- **Addition:** `drip`
- **Subtraction:** `lack`
- **Multiplication:** `combo`
- **Division:** `ratio`
- **Equality:** `no cap`
- **Inequality:** `cap`
  ```brainrot
  vibe check (score cap 100) {
      flex "Score is not 100"
  }
  ```

---

#### **Classes**

- **Class Definition:** `squad goals`
- **Friend Class:** `blud`
- **Public Member:** `highkey`
- **Private Member:** `lowkey`
- **Protected Member:** `guarded af`
- **Create Instance:** `cook`
- **Deallocate Instance:** `cooked`
  ```brainrot
  squad goals Person {
      highkey name quote
      guarded af age stack

      dms __init__ quote person_name stack person_age {
          this.name = person_name
          this.age = person_age
      }
  }

  beta p cook Person "John" 30
  cooked p
  ```

---

#### **Exceptions**

- **Throw Exception:** `yeet`
- **Error Type:** `red flag`
- **Try Block:** `send it`
- **Catch Block:** `caught in 4k`
- **Finally Block:** `last chance bro`
  ```brainrot
  send it {
      vibe check (age < 18) {
          yeet red flag "Underage error"
      }
  } caught in 4k red flag {
      flex "Caught error: Underage"
  } last chance bro {
      flex "End of try-catch"
  }
  ```

---

This specification outlines the syntax and structure of **Brainrot**, a humorously designed language for programmers looking for an alternative way to approach logic and structure. The expressive language elements make coding almost conversational while keeping to traditional programming principles.
