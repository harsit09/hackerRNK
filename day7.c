int main(){
    int n,m=0; 
    scanf("%d",&n);
    int *arr = malloc(sizeof(int) * n);
    for(int arr_i = 0; arr_i < n; arr_i++){
       scanf("%d",&arr[arr_i]);
    }
    for(int arr_j=n-1;arr_j >=0; arr_j--){
        printf("%d ", arr[arr_j]);
    }
    return 0;
}
