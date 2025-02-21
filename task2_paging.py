import matplotlib.pyplot as plt
import numpy as np

class PageTable:
    def __init__(self, num_pages):
        self.table = [-1] * num_pages  # -1 indicates page not in memory

    def update(self, page, frame):
        self.table[page] = frame

    def get_frame(self, page):
        return self.table[page]

def simulate_paging():
    physical_memory_size = int(input("Enter size of physical memory: "))
    page_size = int(input("Enter page size: "))
    page_requests = list(map(int, input("Enter sequence of page requests (space-separated): ").split()))

    num_frames = physical_memory_size // page_size
    num_pages = max(page_requests) + 1
    page_table = PageTable(num_pages)
    memory = [-1] * num_frames  # -1 indicates empty frame
    page_fault_count = 0
    current_frame = 0

    fig, axs = plt.subplots(len(page_requests), 1, figsize=(10, 3*len(page_requests)))
    fig.suptitle("Memory State After Each Request")

    for i, page in enumerate(page_requests):
        if page_table.get_frame(page) == -1:  # Page fault
            page_fault_count += 1
            if current_frame < num_frames:
                memory[current_frame] = page
                page_table.update(page, current_frame)
                current_frame += 1
            else:
                # Simple FIFO replacement
                victim = memory.pop(0)
                memory.append(page)
                page_table.update(victim, -1)
                page_table.update(page, num_frames - 1)

        # Visualize memory state
        ax = axs[i] if len(page_requests) > 1 else axs
        ax.bar(range(num_frames), [1]*num_frames, color='lightgray')
        for j, p in enumerate(memory):
            if p != -1:
                ax.text(j, 0.5, f'P{p}', ha='center', va='center')
        ax.set_ylim(0, 1)
        ax.set_yticks([])
        ax.set_xlabel('Frames')
        ax.set_title(f'After request: Page {page}')

    plt.tight_layout()
    plt.show()

    print("\nFinal Page Table:")
    for i, frame in enumerate(page_table.table):
        print(f"Page {i}: Frame {frame}")
    print(f"\nTotal Page Faults: {page_fault_count}")

simulate_paging()