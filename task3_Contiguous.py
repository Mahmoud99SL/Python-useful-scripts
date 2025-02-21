import matplotlib.pyplot as plt

def allocate_files_contiguously(num_files, file_sizes, available_blocks):
    # Create an allocation table to track which blocks are allocated to which files
    allocation_table = [-1] * len(available_blocks)  # -1 means block is free
    current_block = 0  # Start allocating from the first block

    # List to keep track of the memory state for visualization
    memory_state = []

    # Iterate over each file to allocate space
    for file_index in range(num_files):
        file_size = file_sizes[file_index]
        # Check if there is enough contiguous space available
        if current_block + file_size <= len(available_blocks):
            # Allocate blocks for this file
            for i in range(file_size):
                allocation_table[current_block + i] = file_index  # Mark block as allocated to this file
            memory_state.append(allocation_table.copy())  # Save the current state of memory
            current_block += file_size  # Move to the next available block
        else:
            print(f"File {file_index} of size {file_size} cannot be allocated due to insufficient space.")
            memory_state.append(allocation_table.copy())  # Save the current state even if allocation fails

    return allocation_table, memory_state

def visualize_memory_state(memory_state, num_files):
    # Set up the plot
    fig, axs = plt.subplots(len(memory_state), 1, figsize=(10, 3 * len(memory_state)))
    fig.suptitle("Memory State After Each Allocation Request")

    # Iterate through each memory state and plot it
    for i, state in enumerate(memory_state):
        axs[i].bar(range(len(state)), [1] * len(state), color='lightgray')  # Draw all blocks as light gray
        for block_index, file_index in enumerate(state):
            if file_index != -1:  # If the block is allocated
                axs[i].text(block_index, 0.5, f'F{file_index}', ha='center', va='center', color='black')
        axs[i].set_ylim(0, 1)
        axs[i].set_yticks([])
        axs[i].set_xlabel('Disk Blocks')
        axs[i].set_title(f'After Allocating File(s)')

    plt.tight_layout()
    plt.show()

def main():
    # Get user input for number of files
    num_files = int(input("Enter the number of files: "))
    
    # Get sizes of each file from the user
    file_sizes = []
    for i in range(num_files):
        size = int(input(f"Enter size of file {i + 1}: "))
        file_sizes.append(size)

    # Get available disk blocks from the user
    total_blocks = int(input("Enter the total number of available disk blocks: "))
    available_blocks = [0] * total_blocks  # Initialize available blocks (not used directly but for reference)

    # Allocate files contiguously and get the allocation table and memory states
    allocation_table, memory_state = allocate_files_contiguously(num_files, file_sizes, available_blocks)

    # Print out the allocation table
    print("\nAllocation Table:")
    for block_index, allocated_file in enumerate(allocation_table):
        if allocated_file != -1:
            print(f"Block {block_index}: File {allocated_file}")
        else:
            print(f"Block {block_index}: Free")

    # Visualize how files are stored in disk blocks after each request
    visualize_memory_state(memory_state, num_files)

# Run the program
if __name__ == "__main__":
    main()