// Delay
// Program 027

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program027.generated.h"

UCLASS()
class AProgram027 : public AActor
{
    GENERATED_BODY()

public:
    AProgram027();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
