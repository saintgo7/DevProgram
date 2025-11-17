// Blueprint Library
// Program 024

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program024.generated.h"

UCLASS()
class AProgram024 : public AActor
{
    GENERATED_BODY()

public:
    AProgram024();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
