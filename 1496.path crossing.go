type Point struct {
    X, Y int
}

func isPathCrossing(path string) bool {
    visited := make(map[Point]bool)
    point := Point{0, 0}
    visited[point] = true
    
    for _, move := range path {
        switch move {
            case 'N':
            point.Y -= 1
            case 'S':
            point.Y += 1
            case 'E':
            point.X += 1
            case 'W':
            point.X -= 1
        }
        if visited[point] {
            return true
        }
        visited[point] = true
    }
    return false
}