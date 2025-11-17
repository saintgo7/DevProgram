// Animation Montage

#include "Program033.h"

AProgram033::AProgram033()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram033::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Animation Montage ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating animation montage."));

    // Implement the program logic here...
}

void AProgram033::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
