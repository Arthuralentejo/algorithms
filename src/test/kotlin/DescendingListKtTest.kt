import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class DescendingListKtTest {

    @Test
    fun descendingList() {
        assertEquals(listOf(56,41,24,15,12),descendingList(listOf(15,24,41,12,56)))
    }
}