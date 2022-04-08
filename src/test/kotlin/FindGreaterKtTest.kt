import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class FindGreaterKtTest {

    @Test
    fun findGreater() {
        assertEquals(10, findGreater(listOf<Int>(2,5,8,10)))
    }
}