// Timer

#include "Program026.h"

AProgram026::AProgram026()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram026::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Timer ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating timer."));

    // Implement the program logic here...
}

void AProgram026::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
