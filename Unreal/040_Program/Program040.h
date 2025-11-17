// Nav Mesh
// Program 040

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program040.generated.h"

UCLASS()
class AProgram040 : public AActor
{
    GENERATED_BODY()

public:
    AProgram040();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
