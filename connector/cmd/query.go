package cmd

import (
	"fmt"
	"github.com/spf13/cobra"
)

var queryCMD = &cobra.Command {
	Use: "query",
	Short: "run a query against Trino.",
	Long: "The query command runs a sql query against Trino and prints the results",
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("Quering Trino")

		http := ""
		prompt := &survey.Select{
			Message: "Choose an HTTP Method:",
			Options: []string {"GET", "POST", "PATCH", "PUT", "DELETE"},
		},
	},
},

func init() {
	rootCMD.AddCommand(queryCMD)
}