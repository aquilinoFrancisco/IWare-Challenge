import static org.junit.jupiter.api.Assertions.*;
import org.junit.Before;
import org.junit.jupiter.api.Test;

class AreaTest {

	private Area area;

	@Test
	void testComputeArea() {
		assertEquals(196, area.computeArea(-7,-7,7,7,-1,-1,-5,-5), 0);
	}
}
