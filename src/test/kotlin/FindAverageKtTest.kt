import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class FindAverageKtTest {

    @Test
    fun findAverage() {
        assertEquals(7.5,findAverage(listOf(8,9,7,6)))
    }
}