// Cascade

#include "Program073.h"

AProgram073::AProgram073()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram073::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Cascade ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating cascade."));

    // Implement the program logic here...
}

void AProgram073::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
