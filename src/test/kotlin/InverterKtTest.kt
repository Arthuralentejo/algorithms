import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class InverterKtTest {

    @Test
    fun inverter(){
        assertEquals(listOf(5,4,3,2,1), inverter(listOf(1,2,3,4,5)))
    }
}