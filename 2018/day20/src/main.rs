use std::{
    cmp::max,
    collections::{HashMap, HashSet, VecDeque},
    io::{self, Read, Write},
    ops::Add,
    time::Instant,
};

fn main() {
    let mut input = Vec::new();
    io::stdin().read_to_end(&mut input).unwrap();

    let regex = input.trim_ascii();
    let regex = &regex[1..regex.len() - 1];

    eprintln!("[init] regex length: {} characters", regex.len());

    let mut graph: HashMap<Point, HashSet<Point>> = HashMap::new();
    build_graph(regex, &mut graph);

    eprintln!(
        "[graph] {} rooms, {} total directed edges",
        graph.len(),
        graph.values().map(|s| s.len()).sum::<usize>()
    );

    let (p1, p2) = bfs(&graph, Point::ORIGIN);
    println!("{p1}");
    println!("{p2}");
}

const PROGRESS_EVERY: usize = 10_000;

/// Walk the regex iteratively, inserting undirected edges into `graph`.
fn build_graph(regex: &[u8], graph: &mut HashMap<Point, HashSet<Point>>) {
    let total = regex.len();
    let mut curr: HashSet<Point> = [Point::ORIGIN].into();
    let mut stack: Vec<(HashSet<Point>, HashSet<Point>)> = Vec::new();
    let t0 = Instant::now();

    for (i, &b) in regex.iter().enumerate() {
        if i % PROGRESS_EVERY == 0 {
            let pct = i * 100 / total;
            eprint!(
                "\r[build_graph] {i}/{total} ({pct}%)  \
                 stack depth: {:2}  \
                 frontier: {:4}  \
                 rooms: {:6}  \
                 elapsed: {:.1}s  ",
                stack.len(),
                curr.len(),
                graph.len(),
                t0.elapsed().as_secs_f32(),
            );
            io::stderr().flush().unwrap();
        }

        match b {
            b'(' => {
                stack.push((curr.clone(), HashSet::new()));
            }
            b'|' => {
                let (entry, exits) = stack.last_mut().unwrap();
                exits.extend(&curr);
                curr = entry.clone();
            }
            b')' => {
                let (_, mut exits) = stack.pop().unwrap();
                exits.extend(curr);
                curr = exits;
            }
            _ => {
                let dir = Point::from_direction(b);
                curr = curr
                    .iter()
                    .map(|&p| {
                        let next = p + dir;
                        graph.entry(p).or_default().insert(next);
                        graph.entry(next).or_default().insert(p);
                        next
                    })
                    .collect();
            }
        }
    }

    eprintln!(
        "\r[build_graph] done. {total}/{total} (100%)  \
         rooms: {}  elapsed: {:.2}s                    ",
        graph.len(),
        t0.elapsed().as_secs_f32(),
    );
}

/// BFS from `start`.
/// Returns (maximum shortest-path distance, number of rooms at distance ≥ 1000).
fn bfs(graph: &HashMap<Point, HashSet<Point>>, start: Point) -> (u32, u32) {
    let total = graph.len();
    let mut seen = HashSet::from([start]);
    let mut queue = VecDeque::from([(start, 0u32)]);
    let mut longest = 0;
    let mut far_rooms = 0;
    let mut visited = 0usize;
    let t0 = Instant::now();

    while let Some((curr, dist)) = queue.pop_front() {
        visited += 1;
        longest = max(longest, dist);
        if dist >= 1000 {
            far_rooms += 1;
        }

        if visited % PROGRESS_EVERY == 0 {
            let pct = visited * 100 / total;
            eprint!(
                "\r[bfs] visited: {visited}/{total} ({pct}%)  \
                 queue: {:5}  \
                 max_dist_so_far: {longest:5}  \
                 far_rooms: {far_rooms}  \
                 elapsed: {:.1}s  ",
                queue.len(),
                t0.elapsed().as_secs_f32(),
            );
            io::stderr().flush().unwrap();
        }

        for &next in &graph[&curr] {
            if seen.insert(next) {
                queue.push_back((next, dist + 1));
            }
        }
    }

    eprintln!(
        "\r[bfs] done. visited: {visited}/{total} (100%)  \
         max_dist: {longest}  \
         far_rooms: {far_rooms}  \
         elapsed: {:.2}s                    ",
        t0.elapsed().as_secs_f32(),
    );

    (longest, far_rooms)
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
struct Point {
    x: i32,
    y: i32,
}

impl Point {
    const ORIGIN: Self = Self { x: 0, y: 0 };

    fn from_direction(b: u8) -> Self {
        match b {
            b'N' => Self { x: 0, y: 1 },
            b'S' => Self { x: 0, y: -1 },
            b'E' => Self { x: 1, y: 0 },
            b'W' => Self { x: -1, y: 0 },
            _ => panic!("unexpected character: {}", b as char),
        }
    }
}

impl Add for Point {
    type Output = Self;
    fn add(self, other: Self) -> Self {
        Self {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
}
