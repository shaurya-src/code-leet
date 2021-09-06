class Solution:
    def divisorGame(self, n: int) -> bool:
        # Let's assume if N -> even
        # then aAlice will always select 1 and now remaining N-1 (odd) will transferred to bob
        # We know that odd numbers have odd factors
        # Like: 15 -> 1,3,5,15 but we can't take 15 as 0<x<N
        # So if Bob will take any factor then [n(odd)-any odd number]=even
        # Then alice have now again an even number and he will follow same strategy
        # At last bob will get 1 and bob have to take move 0<x<N
        # So no number is greater than 0 and less than 1, so bob will loose the game
        # because he can't take move

        # If N -> odd then it will be reverse for ALICE every time Bob will take previous 
        # explained moves and Alice will always loose
        
        return n%2 == 0