// Animation Montage
// Program 033

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program033.generated.h"

UCLASS()
class AProgram033 : public AActor
{
    GENERATED_BODY()

public:
    AProgram033();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
