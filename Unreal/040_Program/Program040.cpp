// Nav Mesh

#include "Program040.h"

AProgram040::AProgram040()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram040::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Nav Mesh ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating nav mesh."));

    // Implement the program logic here...
}

void AProgram040::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
