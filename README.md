# Shut the Box

<img src="images/original.jpg" width="830">

## How to play
1. Flip all the tiles UP
1. Roll the dice
1. Flip DOWN tiles that add up to total number rolled
1. Continue rolling until:
  * Last tiles flipped down, player wins
  * No combination can be flipped down, player loses

```mermaid
flowchart TD
    A[Start] --> B[Flip all tiles UP]
    B --> C[Roll the dice]
    C --> D{Can tiles be flipped down to match the roll?}
    D -->|Yes| E[Flip DOWN tiles that add up to total number rolled]
    E --> C
    D -->|No| F[Player loses]
    E --> G{Are all tiles flipped down?}
    G -->|Yes| H[Player wins]
    G -->|No| C
```


## Simulate the game and find optimal strategy
```
def main():
    '''
    Simulate a game of Shut the Box using different strategies and report the win rate.
    '''
    
    iterations = 100_000

    stratagies = [random_tiles, 
                  highest_tile, 
                  fewest_tiles, 
                  most_tiles, 
                  expirement, 
                  adaptive_strategy, 
                  prioritize_low_high]

    # Run the game for each strategy
    for stratagy in stratagies:
        print(f"stratagy: {stratagy.__name__}")

        wins = 0
        for i in range(iterations):
            wins += play(stratagy)

        # report strategy win rate  as a percentage
        print(f"Win Rate: {wins / iterations * 100:.2f}%")      

        # report stratey win rate as number of times you have to play to expect a win
        print(f"Win Rate: {1 / (wins / iterations):.0f} games\n")  
```

## Create a version of the game with a laser cutter
<img src="images/laser_print.png"/>

Shut the Box
## Useful Links

Here are some useful links for creating a version of the game with a laser cutter and purchasing materials:

### Laser Cutter Box Designs from [Boxes.PY](https://boxes.hackerspace-bamberg.de/?language=en)
- [Top](https://boxes.hackerspace-bamberg.de/ABox?FingerJoint_style=rectangular&FingerJoint_surroundingspaces=2.0&FingerJoint_bottom_lip=0.0&FingerJoint_edge_width=1.0&FingerJoint_extra_length=0.0&FingerJoint_finger=2.0&FingerJoint_play=0.0&FingerJoint_space=2.0&FingerJoint_width=1.0&Lid_handle=none&Lid_style=none&Lid_handle_height=8.0&Lid_height=4.0&Lid_play=0.1&x=265&y=200&h=30&outside=0&outside=1&bottom_edge=h&thickness=3.0&format=svg&tabs=0.0&qr_code=0&debug=0&labels=0&labels=1&reference=100.0&inner_corners=loop&burn=0.1&language=en&render=0)
- [Bottom](https://boxes.hackerspace-bamberg.de/ABox?FingerJoint_style=rectangular&FingerJoint_surroundingspaces=2.0&FingerJoint_bottom_lip=0.0&FingerJoint_edge_width=1.0&FingerJoint_extra_length=0.0&FingerJoint_finger=2.0&FingerJoint_play=0.0&FingerJoint_space=2.0&FingerJoint_width=1.0&Lid_handle=none&Lid_style=none&Lid_handle_height=8.0&Lid_height=4.0&Lid_play=0.1&x=265&y=200&h=40&outside=0&outside=1&bottom_edge=h&thickness=3.0&format=svg&tabs=0.0&qr_code=0&debug=0&labels=0&labels=1&reference=100.0&inner_corners=loop&burn=0.1&language=en&render=0)
- [Top Anchor Insert](https://boxes.hackerspace-bamberg.de/ABox?FingerJoint_style=rectangular&FingerJoint_surroundingspaces=2.0&FingerJoint_bottom_lip=0.0&FingerJoint_edge_width=1.0&FingerJoint_extra_length=0.0&FingerJoint_finger=2.0&FingerJoint_play=0.0&FingerJoint_space=2.0&FingerJoint_width=1.0&Lid_handle=none&Lid_style=none&Lid_handle_height=8.0&Lid_height=4.0&Lid_play=0.1&x=262&y=197&h=28&outside=0&outside=1&bottom_edge=h&thickness=3.0&format=svg&tabs=0.0&qr_code=0&debug=0&labels=0&labels=1&reference=100.0&inner_corners=loop&burn=0.1&language=en&render=0)
- [Peg Holder insert](https://boxes.hackerspace-bamberg.de/ABox?FingerJoint_style=rectangular&FingerJoint_surroundingspaces=2.0&FingerJoint_bottom_lip=0.0&FingerJoint_edge_width=1.0&FingerJoint_extra_length=0.0&FingerJoint_finger=2.0&FingerJoint_play=0.0&FingerJoint_space=2.0&FingerJoint_width=1.0&Lid_handle=none&Lid_style=none&Lid_handle_height=8.0&Lid_height=4.0&Lid_play=0.1&x=262&y=55&h=30&outside=0&outside=1&bottom_edge=h&thickness=3.0&format=svg&tabs=0.0&qr_code=0&debug=0&labels=0&labels=1&reference=100.0&inner_corners=loop&burn=0.1&language=en&render=0)

### Purchase Materials
- [1/8" Baltic Birch Plywood Sheets](https://www.amazon.com/Premium-Baltic-Plywood-Sheets-Woodpeckers/dp/B07NWYZJ3M/ref=mp_s_a_1_1_sspa?crid=3PRF5KMGAN6WL&dib=eyJ2IjoiMSJ9.dP3lAm-3PhXd7Ydx6-kmb5gkpGDtaBlGvuYW4Ta5LzP_7ZLfHRXgDKbXuKIqnLqitCLjtb-yT7-ByFSqQeClRdbf3sK5tyIeIZmT_g6hzp-mhZvHpSDf7pHOqzWqaiypANbale2Tg5JVVJBTrS6eCCVlFn2luo8gr_6fP8vOKfgHRxodXOIWpMhE0QztM04h2JgdbLLFA9uBAMrhVXHfvQ.uPxLmHTHmQmJC-pTKVnwUSlOfE3Sz7-blfA5uzxFA5w&dib_tag=se&keywords=1%2F8%2Bbaltic%2Bbirch%2Bplywood%2B12x20&qid=1730488850&sprefix=1%2F8%2Bbal%2Caps%2C109&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9waG9uZV9zZWFyY2hfYXRm&th=1)

