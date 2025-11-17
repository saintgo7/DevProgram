// USkeletalMeshComponent

#include "Program020.h"

AProgram020::AProgram020()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram020::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== USkeletalMeshComponent ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating uskeletalmeshcomponent."));

    // Implement the program logic here...
}

void AProgram020::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
