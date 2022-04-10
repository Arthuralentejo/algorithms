import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class PalidromeKtTest {

    @Test
    fun isPalidrome() {
        val phrase =  "Adias a data da saida"
        assertTrue(isPalidrome(phrase))
    }
}