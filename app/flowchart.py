import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create figure and axes
fig, ax = plt.subplots(figsize=(14, 10))

# Set axis limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)

# Remove axes
ax.axis('off')

# Create flowchart boxes and arrows
def add_box(ax, text, x, y, width=2, height=1, boxstyle="round,pad=0.3"):
    box = patches.FancyBboxPatch((x, y), width, height, boxstyle=boxstyle, edgecolor="black", facecolor="lightgrey")
    ax.add_patch(box)
    ax.text(x + width / 2, y + height / 2, text, ha="center", va="center", fontsize=12)

def add_arrow(ax, x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->", lw=1.5))

# Main process flow
add_box(ax, "Start", 4, 13)
add_box(ax, "User Input:\nNatural Language Query", 4, 11)
add_box(ax, "FastAPI Endpoint:\n/generate_and_execute_sql/", 4, 9)
add_box(ax, "Function:\ngenerate_and_execute_sql", 4, 7)
add_box(ax, "Module:\nopenai_rag", 4, 5)
add_box(ax, "Retrieve Contexts\nfrom Vector Store", 4, 3)
add_box(ax, "Generate SQL Query\nwith OpenAI", 4, 1)
add_box(ax, "Module:\nsql_executor", 4, -1)
add_box(ax, "Execute SQL Query\non PostgreSQL", 4, -3)
add_box(ax, "Return SQL Query\nand Execution Result", 4, -5)
add_box(ax, "Display Results\nto User", 4, -7)
add_box(ax, "End", 4, -9)

# Arrows for main process
add_arrow(ax, 5, 13, 5, 12)
add_arrow(ax, 5, 11, 5, 10)
add_arrow(ax, 5, 9, 5, 8)
add_arrow(ax, 5, 7, 5, 6)
add_arrow(ax, 5, 5, 5, 4)
add_arrow(ax, 5, 3, 5, 2)
add_arrow(ax, 5, 1, 5, 0)
add_arrow(ax, 5, -1, 5, -2)
add_arrow(ax, 5, -3, 5, -4)
add_arrow(ax, 5, -5, 5, -6)
add_arrow(ax, 5, -7, 5, -8)

# Vector store processing subgraph
add_box(ax, "Start", 0, 6, width=2, height=1, boxstyle="round,pad=0.3")
add_box(ax, "Process PDF:\ntable_descriptions.pdf", 0, 4, width=2, height=1, boxstyle="round,pad=0.3")
add_box(ax, "Create Embeddings", 0, 2, width=2, height=1, boxstyle="round,pad=0.3")
add_box(ax, "Store Embeddings\nin Qdrant", 0, 0, width=2, height=1, boxstyle="round,pad=0.3")
add_box(ax, "End", 0, -2, width=2, height=1, boxstyle="round,pad=0.3")

# Arrows for vector store processing
add_arrow(ax, 1, 6, 1, 5)
add_arrow(ax, 1, 4, 1, 3)
add_arrow(ax, 1, 2, 1, 1)
add_arrow(ax, 1, 0, 1, -1)

# Dashed arrows linking main process to vector store processing
ax.annotate("", xy=(2, 5), xytext=(4, 5), arrowprops=dict(arrowstyle="->", lw=1.5, linestyle="dashed"))
ax.annotate("", xy=(2, 0), xytext=(4, 3), arrowprops=dict(arrowstyle="->", lw=1.5, linestyle="dashed"))

# Save as SVG
output_path = "natural_language_sql_generator_flowchart.svg"
plt.savefig(output_path, format="svg")

# Close the plot to release resources
plt.close()

output_path
