package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
)

// generateCmd represents the generate command
var generateCmd = &cobra.Command{
	Use:   "generate",
	Short: "Generates a SQL query from a natural language prompt.",
	Long:  `The generate command takes a natural language prompt and uses an LLM to generate a valid SQL query.`,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("generate command called")
	},
}

func init() {
	rootCmd.AddCommand(generateCmd)
}